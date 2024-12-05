from pydantic import BaseModel
from datetime import datetime, date
from typing import List
from src.report.schemas import Follow_Up_Response_Model
import uuid


class ReportResponseModel(BaseModel):
    report_id: str
    description: str
    agency_id: uuid.UUID
    date_created: datetime
    follow_ups: List[Follow_Up_Response_Model] | None

class ReportCreateModel(BaseModel):
    description: str
    agency_id: uuid.UUID

class Follow_Up_Response_Model(BaseModel):
    follow_up_id: uuid.UUID
    description: str
    report_id: str
    date_created: datetime

class Follow_Up_Create_Model(BaseModel):
    description: str

