from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.db.models.job import Job, JobStatus

router = APIRouter(tags=["Result"])

@router.get("/result/{job_id}")
async def get_result(job_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Job).where(Job.id == job_id)
    result = await db.execute(stmt)
    job = result.scalar_one_or_none()
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job with ID '{job_id}' not found.")
    if job.status != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=400, 
            detail=f"Job not finished yet. Current status is: {job.status.value}"
        )
    return {
        "job_id": job.id, 
        "status": "success",
        "report": {
            "message": "Data cleaning processing engine successfully validated this column structure.",
            "raw_log_reference": job.error_message if job.error_message else "No anomalies detected."
        }
    }
    
    
