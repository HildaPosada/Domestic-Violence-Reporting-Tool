from pydantic import BaseModel
from datetime import datetime
import uuid

class AgencyResponseModel(BaseModel):
    agency_id: uuid.UUID
    agency_name: str
    email: str
    phone_number: str
    is_activated: bool
    agency_type: str
    date_created: datetime

class AgencyCreateModel(BaseModel):
    agency_name: str
    email: str
    phone_number: str
    agency_type: str