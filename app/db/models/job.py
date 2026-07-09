from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from datetime import datetime, UTC
from enum import Enum
from app.db.base import Base

class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class Job(Base):
    __tablename__ = "jobs"
    id: Mapped[int] = mapped_column(primary_key=True)
    original_filename: Mapped[str] = mapped_column(String(255),nullable = False)
    status: Mapped[JobStatus] = mapped_column(default= JobStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now(UTC))
    completed_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now(UTC))
    error_message:Mapped[str] = mapped_column(String(255),nullable= True)
    output_file_path:Mapped[str] = mapped_column(String(255),nullable = True)




