from pydantic import BaseModel
from datetime import datetime, date
import uuid


class User(BaseModel):
    pass


class UserCreateModel(BaseModel):
    pass


class UserUpdateModel(BaseModel):
    pass