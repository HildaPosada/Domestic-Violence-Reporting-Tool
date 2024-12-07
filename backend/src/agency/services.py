from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from fastapi.exceptions import HTTPException
from fastapi import status
from src.report.models import Report, Follow_Up_Reports
from src.agency.models import Agency
from sqlalchemy.orm import joinedload
from src.utils import custom_uuid
from src.utils.map import all_reports, all_agencies
from src.exception_handler.global_exception import NotFoundException
import uuid


class AgencyService:
    # get all agency reports
    async def get_all_agency_reports(self, agency_id: uuid.UUID, session: AsyncSession):
        query = (
            select(Report)
            .where(Report.agency_uid == agency_id and Report.is_active)
            .options(joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        reports = results.all()

        if reports is None:
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail=f"No report found for agency")

        response = all_reports(reports)

        return response

    # get agency
    async def get_agency(self, agency_id: uuid.UUID, session: AsyncSession):
        query = (
            select(Agency)
            .join(Follow_Up_Reports)
            .where(Agency.uid == agency_id)
            .options(joinedload(Agency.reports))
            .options(joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        agency = results.one_or_none()

        if agency is None:
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail="Agency not found")

        response = all_agencies([agency])

        return response

    # get all agency
    async def get_all_agencies(self, session: AsyncSession):
        query = (
            select(Agency)
            .join(Follow_Up_Reports)
            .options(joinedload(Agency.reports))
            .options(joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        agencies = results.all()

        if agencies is None:
            return NotFoundException(
                status.HTTP_404_NOT_FOUND, detail="No agency found"
            )

        response = all_agencies(agencies)

        return response

    # get all active agencies
    async def get_active_agencies(self, session: AsyncSession):
        query = (
            select(Agency)
            .join(Follow_Up_Reports)
            .where(Agency.is_activated)
            .options(joinedload(Agency.reports))
            .options(joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        agencies = results.all()

        if agencies is None:
            return NotFoundException(
                status.HTTP_404_NOT_FOUND, detail="No active agency"
            )
        
        response = all_agencies(agencies)
        
        return response


    # get all inactive agencies
    # create agaency
    # deactivate agency
    # update agency details
