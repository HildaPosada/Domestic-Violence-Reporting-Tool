from pydantic import BaseModel, Field
from datetime import datetime
import uuid
from typing import List
from src.report.schemas import ReportResponseModel


class AgencyResponseModel(BaseModel):
    agency_id: uuid.UUID
    agency_name: str
    email: str
    address: str
    phone_number: str
    is_activated: bool
    agency_type: str
    date_created: datetime
    reports: List[ReportResponseModel] | None

class AgencyCreateModel(BaseModel):
    agency_name: str
    email: str = Field(max_length=254)
    phone_number: str = Field(max_length=20)
    address: str = Field(max_length=500)
    agency_type: str
    password: str = Field(min_length=6)

class AgencyUpdateModel(BaseModel):
    agency_name: str
    email: str = Field(max_length=254)
    phone_number: str = Field(max_length=20)
    address: str = Field(max_length=500)
    agency_type: str

class AgencyLoginModel(BaseModel):
    email: str
    password: str