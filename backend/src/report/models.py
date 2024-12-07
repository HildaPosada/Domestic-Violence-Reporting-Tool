import uuid
from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.types as sa_types
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import Optional, List
from src.utils.custom_uuid import short_id
from src.agency.models import Agency


class Report(SQLModel, table=True):
    __tablename__ = "reports"

    uid: str = Field(
        sa_column=Column(
            sa_types.String(8), nullable=False, primary_key=True, default=short_id
        )
    )

    description: str = Field(nullable=False)
    agency_uid: uuid.UUID = Field(foreign_key="agencies.uid", nullable=False)
    user_uid: Optional[uuid.UUID] = Field(foreign_key="users.uid", nullable=True)  # Allow user_uid to be optional for anonymous reports
    is_active: bool = Field(default=True)  # Changed default to `True` to reflect active reports
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now, nullable=False))

    follow_up_reports: List["Follow_Up_Reports"] = Relationship(back_populates="report")
    user: Optional["src.auth.models.User"] = Relationship(back_populates="reports")
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
    is_active: bool = Field(default=True)  # Changed default to `True` to reflect active follow-ups
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now, nullable=False))
    report: "Report" = Relationship(back_populates="follow_up_reports")

    def __repr__(self):
        return f"<FollowUp(uid={self.uid}, description={self.description})>"
