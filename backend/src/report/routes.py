from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.report.services import ReportService
from src.report.schemas import ReportCreateModel, ReportUpdateModel, ReportResponseModel, Follow_Up_Create_Model, Follow_Up_Response_Model
from src.db.main import get_session
from typing import List
import uuid

report_router = APIRouter()
report_service = ReportService()

#region REPORT ENDPOINTS
@report_router.get("/", response_model=List[ReportResponseModel])
async def get_all_reports(session: AsyncSession = Depends(get_session)):
    result = await report_service.get_all_reports(session)
    print(result)
    return result

@report_router.get("/{username}", status_code=status.HTTP_200_OK, response_model=List[ReportResponseModel])
async def get_all_user_reports(username: str, session: AsyncSession = Depends(get_session)) -> dict:
    print(username)
    result = await report_service.get_all_user_reports(username, session)
    return result

@report_router.get("/report/{report_id}", status_code=status.HTTP_200_OK, response_model=List[ReportResponseModel])
async def get_report(report_id: str, session: AsyncSession = Depends(get_session)) -> dict:
    print(report_id)
    result = await report_service.get_report(report_id, session)
    return result

@report_router.post("/create-report", status_code=status.HTTP_201_CREATED, response_model=dict)
async def create_report(user_data: ReportCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    report_id = await report_service.create_report(user_data, session)
    return {"reportId": report_id}

@report_router.put("/update/{username}/{report_id}", status_code=status.HTTP_200_OK)
async def update_report(username: str, report_id: str, user_data: ReportUpdateModel, session: AsyncSession = Depends(get_session)):
    print(user_data)
    result = await report_service.update_report(username, report_id, user_data, session)
    return result
#endregion

#region FOLLOW UP REPORTS ENDPOINTS
@report_router.get("/get-all-follow-up-reports/{report_id}", status_code=status.HTTP_200_OK, response_model=List[Follow_Up_Response_Model])
async def get_all_follow_up_reports(report_id: str, session: AsyncSession = Depends(get_session)) -> dict:
    result = await report_service.get_all_follow_ups(report_id, session)
    return result

@report_router.post("/add-follow-up/{report_id}", status_code=status.HTTP_201_CREATED)
async def add_follow_up_report(report_id: str, user_data: Follow_Up_Create_Model, session: AsyncSession = Depends(get_session)) -> dict:
    result = await report_service.add_follow_up(report_id, user_data, session)
    return result
#endregion
