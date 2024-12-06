# from ast import Index
from sqlmodel import SQLModel, Field, Column, Index, Relationship
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import List
import src 
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
    reports: List["src.report.models.Report"] = Relationship(back_populates="user")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


    def __repr__(self):
        return f"<User {self.username}"
