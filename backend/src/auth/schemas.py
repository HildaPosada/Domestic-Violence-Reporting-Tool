from pydantic import BaseModel
from datetime import datetime, date
import uuid


class User(BaseModel):
    uid: uuid.UUID
    username: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


class UserCreateModel(BaseModel):
    username: str