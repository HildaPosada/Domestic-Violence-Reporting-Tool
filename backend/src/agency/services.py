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
from src.agency.schemas import AgencyCreateModel, AgencyUpdateModel, AgencyResponseModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

class AgencyService:
    # get all agency reports
    async def get_all_agency_reports(self, agency_id: uuid.UUID, session: AsyncSession):
        query = (
            select(Report)
            .where(Report.agency_uid == agency_id, Report.is_active)
            .options(joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        reports = results.all()

        if not reports:
            raise NotFoundException(status.HTTP_404_NOT_FOUND,  f"No report found for agency")

        return all_reports(reports)

    # get agency
    async def get_agency(self, agency_id: uuid.UUID, session: AsyncSession):
        query = (
            select(Agency)
            .join(Follow_Up_Reports)
            .where(Agency.uid == agency_id)
            .options(joinedload(Agency.reports), joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        agency = results.one_or_none()

        if not agency:
            raise NotFoundException(status.HTTP_404_NOT_FOUND,  "Agency not found")

        return all_agencies([agency])

    # get all agencies
    async def get_all_agencies(self, session: AsyncSession):
        query = (
            select(Agency)
            .join(Follow_Up_Reports)
            .options(joinedload(Agency.reports), joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        agencies = results.all()

        if not agencies:
            raise NotFoundException(
                status.HTTP_404_NOT_FOUND,  "No agency found"
            )

        return all_agencies(agencies)

    # get all active agencies
    async def get_active_agencies(self, session: AsyncSession):
        query = (
            select(Agency)
            .join(Follow_Up_Reports)
            .where(Agency.is_activated)
            .options(joinedload(Agency.reports), joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        agencies = results.all()

        if not agencies:
            raise NotFoundException(
                status.HTTP_404_NOT_FOUND,  "No active agency"
            )

        return all_agencies(agencies)

    # get all inactive agencies
    async def get_inactive_agencies(self, session: AsyncSession):
        query = (
            select(Agency)
            .join(Follow_Up_Reports)
            .where(Agency.is_activated == False)
            .options(joinedload(Agency.reports), joinedload(Report.follow_up_reports))
        )

        results = await session.exec(query)

        agencies = results.all()

        if not agencies:
            raise NotFoundException(
                status.HTTP_404_NOT_FOUND,  "No inactive agency"
            )

        return all_agencies(agencies)

    # create agency
    async def create_agency(self, agency_data: AgencyCreateModel, session: AsyncSession):
        new_agency = Agency(
            uid=uuid.UUID,
            agency_name= agency_data.agency_name,
            email=agency_data.email,
            phone=agency_data.phone_number,
            agency_type= agency_data.agency_type,
            is_activated=False,
            password_hash= pwd_context.hash(agency_data.password)
        )

        session.add(new_agency)

        await session.commit()

        return status.HTTP_200_OK

    # activate agency
    async def activate_agency(self, agency_id: uuid.UUID, session: AsyncSession) -> str:
        query = select(Agency).where(Agency.uid == agency_id)

        result = await session.exec(query)

        response = result.one_or_none()

        if not response:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "Agency not found")

        if response.is_activated == True:
            return "Agency is already active"

        response.is_activated == True

        session.add(response)
        await session.commit()

        return "Agency activated"

    # deactivate agency
    async def deactivate_agency(self, agency_id: uuid.UUID, session: AsyncSession) -> str:
        query = select(Agency).where(Agency.uid == agency_id)

        result = await session.exec(query)

        response = result.one_or_none()

        if not response:
            return NotFoundException(status.HTTP_404_NOT_FOUND, "Agency not found")

        if response.is_activated == False:
            return "Agency is already active"

        response.is_activated == False

        session.add(response)
        await session.commit()

        return "Agency deactivated"

    # update agency details
    async def update_agency(self, agency_id: uuid.UUID, agency_data: AgencyUpdateModel, session: AsyncSession):
        agencies = await self.get_agency(agency_id, session)

        if not agencies:
            return NotFoundException(status.HTTP_404_NOT_FOUND, "Agency not found")

        for agency in agencies:
            agency.agency_name = agency_data.agency_name
            agency.email = agency_data.email
            agency.phone_number = agency_data.phone_number
            agency.address = agency_data.address
            agency.agency_type = agency_data.agency_type

        session.add_all(agencies)

        await session.commit()

        return status.HTTP_200_OK

    # agency login
    async def agency_login(self, email: str, password: str, session: AsyncSession):
        hashed_password = pwd_context.hash(password)

        query = select(Agency).where(Agency.email == email & Agency.password_hash == hashed_password)

        result = await session.exec(query)

        agency = result.one_or_none()

        if not agency:
            return NotFoundException(status.HTTP_404_NOT_FOUND, f"No agency with this email ({email}) found")

        return status.HTTP_200_OK
