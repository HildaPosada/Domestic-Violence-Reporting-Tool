from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.report.services import ReportService
from src.report.schemas import ReportCreateModel, ReportResponseModel, Follow_Up_Create_Model, Follow_Up_Response_Model
from src.db.main import get_session
from typing import List

report_router = APIRouter()
report_service = ReportService()

#region REPORT ENDPOINTS
@report_router.get("/{username}", status_code=status.HTTP_200_OK, response_model=List[ReportResponseModel])
async def get_all_reports(username: str, session: AsyncSession = Depends(get_session)) -> dict:
    result = await report_service.get_all_user_reports(username, session)
    return result

@report_router.get("/{report_id}", status_code=status.HTTP_200_OK, response_model=ReportResponseModel)
async def get_report(report_id: str, session: AsyncSession = Depends(get_session)) -> dict:
    result = await report_service.get_report(report_id, session)
    return result

@report_router.post("/create-report/{user_id}", status_code=status.HTTP_201_CREATED)
async def create_report(user_id: str, user_data: ReportCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    result = await report_service.create_report(user_id, user_data, session)
    return result

@report_router.put("/update/{user_id}/{report_id}", status_code=status.HTTP_200_OK)
async def update_report(user_id: str, report_id: str, user_data: ReportCreateModel, session: AsyncSession = Depends(get_session)) -> dict:
    result = await report_service.update_report(user_id, report_id, user_data, session)
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