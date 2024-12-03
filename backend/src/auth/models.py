# from ast import Index
from sqlmodel import SQLModel, Field, Column, Index, Relationship
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import List
from src.report.models import Report
import uuid


# User model
class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    username: str
    is_active: bool = Field(default=True)
    reports: List["Report"] = Relationship(back_populates="users")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


    def __repr__(self):
        return f"<User {self.username}"
    

# Agency model
class Agency(SQLModel, table=True):
    __tablename__ = "agencies"


    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    agency_name: str = Field(sa_column=Column(pg.TEXT, unique=True))
    email: str = Field(sa_column=Column(pg.TEXT, unique=True, nullable=False), max_length=254)
    phone: str = Field(sa_column=Column(pg.TEXT), max_length=20)
    address: str = Field(sa_column=Column(pg.TEXT), max_length=500)
    password_hash: str
    is_activated: bool = Field(default=False)
    agency_type: str = Field(default="General")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now))


    __table_args__ = (
        Index('ix_agency_email', 'email'),
        Index('ix_agency_phone', 'phone'),
    )


    def __repr__(self):
        return f"<Agency {self.agency_name}>"