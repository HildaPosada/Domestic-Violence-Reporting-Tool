import uuid
from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.types as sa_types
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import Optional, List
from src.utils.custom_uuid import short_id
from src.agency.models import Agency
import src
from src.report.enums import ReportProgress


class Report(SQLModel, table=True):
    __tablename__ = "reports"

    uid: str = Field(
        sa_column=Column(
            sa_types.String(8), nullable=False, primary_key=True, default=short_id
        )
    )

    username: Optional[str] = Field(default="Anonymous")
    description: str = Field(nullable=False)
    progress: ReportProgress = Field(
        sa_column=Column(
            pg.ENUM(ReportProgress, name="report_progress", create_type=True),
            nullable=False,
            default=ReportProgress.Submitted
        )
    )
    agency_uid: uuid.UUID = Field(foreign_key="agencies.uid", nullable=False, default="3fa85f64-5717-4562-b3fc-2c963f66afa6")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now, nullable=False))

    follow_up_reports: List["Follow_Up_Reports"] = Relationship(back_populates="report")
    agency: "Agency" = Relationship(back_populates="reports")

    def __repr__(self):
        return f"<Report(uid={self.uid}, description={self.description})>"


class Follow_Up_Reports(SQLModel, table=True):
    __tablename__ = "follow_up_reports"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4,
        )
    )
    description: str = Field(nullable=False)
    report_uid: str = Field(foreign_key="reports.uid", nullable=False)
    is_active: bool = Field(default=True)  
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now, nullable=False))
    report: "Report" = Relationship(back_populates="follow_up_reports")

    def __repr__(self):
        return f"<FollowUp(uid={self.uid}, description={self.description})>"
