from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
import uuid
from src.report.enums import ReportProgress


# Schema for creating a follow-up report
class Follow_Up_Create_Model(BaseModel):
    description: str = Field(..., example="This is a follow-up description.")

# Schema for follow-up report response
class Follow_Up_Response_Model(BaseModel):
    follow_up_id: uuid.UUID
    progress: ReportProgress
    report_id: str
    date_created: str

    class Config:
        orm_mode = True


# Schema for creating a report
class ReportCreateModel(BaseModel):
    username: str = Field(default="Anonymous")
    description: str = Field(..., example="This is a description of the incident.")
    agency_id: uuid.UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6")

class ReportUpdateModel(BaseModel):
    description: str = Field(..., example="This is a description of the incident.")
    agency_id: uuid.UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6")

# Schema for report response
class ReportResponseModel(BaseModel):
    user: str
    report_id: str
    progress: ReportProgress
    agency_id: uuid.UUID
    date_created: str
    follow_ups: Optional[List[Follow_Up_Response_Model]] = None

    class Config:
        orm_mode = True
