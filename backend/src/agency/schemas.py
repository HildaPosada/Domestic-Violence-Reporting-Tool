from pydantic import BaseModel
from datetime import datetime
import uuid
from typing import List
from src.report.schemas import ReportResponseModel


class AgencyResponseModel(BaseModel):
    agency_id: uuid.UUID
    agency_name: str
    email: str
    phone_number: str
    is_activated: bool
    agency_type: str
    date_created: datetime
    reports: List[ReportResponseModel] | None

class AgencyCreateModel(BaseModel):
    agency_name: str
    email: str
    phone_number: str
    agency_type: str