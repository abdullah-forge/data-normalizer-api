from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.session import get_db
from app.db.models.job import Job

router = APIRouter(tags=["Status"])

@router.get("/status/{job_id}")
async def get_status(job_id: int, db: AsyncSession = Depends(get_db)):
    # DB se job dhundo: 
    stmt = select(Job).where(Job.id == job_id)
    result = await db.execute(stmt)
    job = result.scalar_one_or_none()
    if job is None:
        raise HTTPException(status_code=404, detail=f"Job with ID '{job_id}' not found.")
    return {
        "job_id": job.id, 
        "status": job.status.value if hasattr(job.status, 'value') else job.status, 
        "filename": job.original_filename
    }

   
