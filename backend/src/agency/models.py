from sqlmodel import SQLModel, Field, Column, Index, Relationship
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import List
import src
import uuid


# Agency model
class Agency(SQLModel, table=True):
    __tablename__ = "agencies"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    agency_name: str = Field(sa_column=Column(pg.TEXT, unique=True))
    email: str = Field(
        sa_column=Column(pg.TEXT, unique=True, nullable=False), max_length=254
    )
    phone: str = Field(sa_column=Column(pg.TEXT), max_length=20)
    password_hash: str
    is_activated: bool = Field(default=False)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    )

    reports: List["src.report.models.Report"] = Relationship(back_populates="agency")

    __table_args__ = (
        Index("ix_agency_email", "email"),
        Index("ix_agency_phone", "phone"),
    )

    def __repr__(self):
        return f"<Agency {self.agency_name}>"
