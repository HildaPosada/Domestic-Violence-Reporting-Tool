from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from typing import List
from src.agency.services import AgencyService
from src.agency.schemas import AgencyResponseModel, AgencyCreateModel, AgencyUpdateModel, AgencyLoginModel
from src.report.schemas import ReportResponseModel, ReportProgress
import uuid

agency_router = APIRouter()
agency_service = AgencyService()

@agency_router.get("/", status_code=status.HTTP_200_OK, response_model=List[AgencyResponseModel])
async def get_all_agencies(session: AsyncSession = Depends(get_session)):
    result = await agency_service.get_all_agencies(session)
    return result

@agency_router.get("/active", status_code=status.HTTP_200_OK, response_model=List[AgencyResponseModel])
async def get_active_agencies(session: AsyncSession = Depends(get_session)):
    result = await agency_service.get_active_agencies(session)
    return result

@agency_router.get("/inactive", status_code=status.HTTP_200_OK, response_model=List[AgencyResponseModel])
async def get_inactive_agencies(session: AsyncSession = Depends(get_session)):
    result = await agency_service.get_inactive_agencies(session)
    return result

@agency_router.get("/{agency_id}", status_code=status.HTTP_200_OK, response_model=List[AgencyResponseModel])
async def get_agency(agency_id: uuid.UUID, session: AsyncSession = Depends(get_session)) -> dict:
    result = await agency_service.get_agency(agency_id, session)
    return result

@agency_router.get("/agency-reports/{agency_id}", status_code=status.HTTP_200_OK, response_model=List[ReportResponseModel])
async def get_agency_reports(agency_id: uuid.UUID, session: AsyncSession = Depends(get_session)) -> dict:
    result = await agency_service.get_all_agency_reports(agency_id, session)
    return result

@agency_router.post("/create-agency", status_code=status.HTTP_200_OK, response_model=None)
async def create_agency(agency_data: AgencyCreateModel, session: AsyncSession = Depends(get_session)):
    result = await agency_service.create_agency(agency_data, session)
    return result

@agency_router.put("/update/agency/{agency_id}", status_code=status.HTTP_200_OK, response_model=None)
async def update_agency(agency_id: uuid.UUID, model: AgencyUpdateModel, session: AsyncSession = Depends(get_session)):
    result = await agency_service.update_agency(agency_id, model, session)
    return result

@agency_router.post("/activate-agency/{agency_id}", status_code=status.HTTP_200_OK, response_model=str)
async def activate_agency(agency_id: uuid.UUID, session: AsyncSession = Depends(get_session)) -> str:
    result = await agency_service.toggle_agency_status(agency_id, True, session)
    return result

@agency_router.post("/deactivate-agency/{agency_id}", status_code=status.HTTP_200_OK, response_model=str)
async def deactivate_agency(agency_id: uuid.UUID, session: AsyncSession = Depends(get_session)) -> str:
    result = await agency_service.toggle_agency_status(agency_id, False, session)
    return result

@agency_router.post("/agency-login", status_code=status.HTTP_200_OK, response_model=str)
async def agency_login(model: AgencyLoginModel, session: AsyncSession = Depends(get_session)) -> str:
    result = await agency_service.agency_login(model, session)
    return result

@agency_router.put("/update-report-status", status_code=status.HTTP_200_OK, response_model=str)
async def update_report_status(report_id: str, status: ReportProgress, session: AsyncSession = Depends(get_session)) -> str:
    result = await agency_service.update_report_status(report_id, status, session)
    return result
