from pydantic import BaseModel, Field
import uuid
from typing import List, Optional
from src.report.schemas import ReportResponseModel, ReportProgress


class AgencyResponseModel(BaseModel):
    agency_id: uuid.UUID
    agency_name: str
    email: str
    phone_number: str
    is_activated: bool
    date_created: str
    reports: Optional[List[ReportResponseModel]] = None

    class Config:
        orm_mode = True

class AgencyReportUpdateModel:
    status: ReportProgress

class AgencyCreateModel(BaseModel):
    agency_name: str
    email: str = Field(max_length=254)
    phone_number: str = Field(max_length=20)
    password: str = Field(min_length=6)

class AgencyUpdateModel(BaseModel):
    agency_name: str
    email: str = Field(max_length=254)
    phone_number: str = Field(max_length=20)

class AgencyLoginModel(BaseModel):
    email: str
    password: str
