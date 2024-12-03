import uuid
from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from src.utils.custom_uuid import short_id
from src.auth.models import User, Agency
# from src.auth.models import Agency
from typing import Optional, List


class Report(SQLModel, table=True):
    __tablename__ = "reports"

    uid: str = Field(
        sa_column=Column(
            nullable=False,
            primary_key=True,
            default=short_id,
        )
    )
    description: str = Field(nullable=False)
    agency_uid: uuid.UUID = Field(foreign_key="agencies.uid", nullable=False)
    user_uid: uuid.UUID | None = Field(foreign_key="users.uid", nullable=False)
    is_active: bool = Field(default=False)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    follow_ups: List["Follow_Up_Reports"] = Relationship(back_populates="reports")
    user: Optional["User"] = Relationship(back_populates="reports")
    agency: "Agency" = Relationship(back_populates="reports")

    def __repr__(self):
        return f"<Report {self.description}"
    

class Follow_Up_Reports(SQLModel, table=True):
    __tablename__ = "follow_up_reports"

    uid: uuid.UUID = Field(
        sa_column=Column(
            nullable=False,
            primary_key=True,
            default=short_id
        )
    )
    description: str = Field(nullable=False)
    report_id: str = Field(foreign_key="reports.uid", nullable=False)
    is_active: bool = Field(default=False)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    report: "Report" = Relationship(back_populates="follow_up_reports")


    def __repr__(self):
        return f"<Follow up {self.description}>"
    