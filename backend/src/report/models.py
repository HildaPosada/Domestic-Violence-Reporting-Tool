from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from src.utils.custom_uuid import short_id
from src.auth.models import User, Agency


class Report(SQLModel, table=True):
    __tablename__ = "reports"

    uid: str = Field(
        sa_column=Column(
            nullable=False,
            primary_key=True,
            default=short_id,
        )
    )
    description: str
    agency_uid: str = Field(foreign_key=Agency.uid)
    user_uid: str = Field(foreign_key=User.uid)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


    def __repr__(self):
        return f"<Report {self.description}"