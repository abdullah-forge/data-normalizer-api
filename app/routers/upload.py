from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
import logging
from pathlib import Path

from app.db.session import get_db
from app.db.models.job import Job, JobStatus
from app.services.processing import process_file
from app.utils.temp_manager import save_temp_file
from app.config.settings import settings

router = APIRouter(tags=["Upload"])
logger = logging.getLogger(__name__)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    file_extension = Path(file.filename).suffix.lower()
    allowed_extensions = [ext.lower() if ext.startswith('.') else f".{ext.lower()}" for ext in settings.allowed_extensions_list]
    if file_extension not in allowed_extensions:
        logger.warning(f"Rejected file with invalid extension: {file.filename}")
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported file extension. Allowed extensions are: {', '.join(settings.allowed_extensions_list)}"
        )

    
    content = await file.read()
    file_size_bytes = len(content)
    if file_size_bytes > settings.max_upload_size_bytes:
        logger.warning(f"File size {file_size_bytes} bytes exceeds maximum allowed limit.")
        raise HTTPException(
            status_code=413, 
            detail=f"File is too large. Maximum allowed size is {settings.max_upload_size_bytes / (10**6)} MB"
        )
    
    extension_raw = file_extension.lstrip('.')
    temp_path = save_temp_file(content, extension_raw)
    
    #new_job = Job(id=str(uuid.uuid4()), original_filename=file.filename, status=JobStatus.PROCESSING)
    new_job = Job(original_filename=file.filename, status=JobStatus.PROCESSING)
    db.add(new_job)
    await db.commit()
    await db.refresh(new_job) 
    
    try:
        report = await process_file(temp_path, file.filename)
        new_job.status = JobStatus.COMPLETED
        new_job.output_file_path = str(temp_path) # temporary
        await db.commit()
        return {"job_id": new_job.id, "message": "File processed successfully", "report": report}
        
    except Exception as e:
        new_job.status = JobStatus.FAILED
        new_job.error_message = str(e)
        await db.commit()
        raise HTTPException(status_code=500, detail="Processing failed")
        
