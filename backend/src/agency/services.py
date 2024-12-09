from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from fastapi import status
from src.report.models import Report, Follow_Up_Reports, ReportProgress
from src.agency.models import Agency
from sqlalchemy.orm import joinedload
from src.report.services import ReportService
from src.utils.map import all_reports, all_agencies
from src.exception_handler.global_exception import NotFoundException, InvalidException
import uuid
from src.agency.schemas import AgencyCreateModel, AgencyUpdateModel, AgencyReportUpdateModel, AgencyLoginModel
from passlib.context import CryptContext
from sqlalchemy.sql.expression import func

pwd_context = CryptContext(schemes=["bcrypt"])


class AgencyService:
    # get all agency reports
    async def get_all_agency_reports(self, agency_id: uuid.UUID, session: AsyncSession):
        query = (
            select(Report)
            .where(Report.agency_uid == agency_id, Report.is_active)
            .options(joinedload(Report.follow_up_reports))
            .order_by(desc(Report.created_at))
        )

        results = await session.exec(query)

        reports = results.all()

        if not reports:
            raise NotFoundException(
                status.HTTP_404_NOT_FOUND, f"No report found for agency"
            )

        return all_reports(reports)

    # get agency
    async def get_agency(self, agency_id: uuid.UUID, session: AsyncSession):
        query = (
            select(Agency)
            .where(Agency.uid == agency_id)
            .order_by(desc(Agency.created_at))
            # .join(Report, Agency.uid == Report.agency_uid)
            # .join(Follow_Up_Reports, Report.uid == Follow_Up_Reports.report_uid)
            # .options(
            #     joinedload(Agency.reports),
            #     joinedload(Agency.reports).joinedload(Report.follow_up_reports),
            # )
        )

        results = await session.exec(query)

        agency = results.one_or_none()

        if not agency:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "Agency not found")

        return all_agencies([agency])

    # get all agencies
    async def get_all_agencies(self, session: AsyncSession):
        query = (
            select(Agency)
            .order_by(desc(Agency.created_at))
            # .join(Report, Agency.uid == Report.agency_uid)
            # .join(Follow_Up_Reports, Report.uid == Follow_Up_Reports.report_uid)
            # .options(
            #     joinedload(Agency.reports),
            #     joinedload(Agency.reports).joinedload(Report.follow_up_reports),
            # )
        )

        results = await session.exec(query)

        agencies = results.all()

        if not agencies:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "No agency found")

        return all_agencies(agencies)

    # get all active agencies
    async def get_active_agencies(self, session: AsyncSession):
        query = (
            select(Agency)
            .where(Agency.is_activated == True)
            .order_by(desc(Agency.created_at))
            # .join(Report, Agency.uid == Report.agency_uid)
            # .join(Follow_Up_Reports, Report.uid == Follow_Up_Reports.report_uid)
            # .options(
            #     joinedload(Agency.reports),
            #     joinedload(Agency.reports).joinedload(Report.follow_up_reports),
            # )
        )

        results = await session.exec(query)

        agencies = results.unique().all()

        print(agencies)

        if not agencies:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "No active agency")

        return all_agencies(agencies)

    # get all inactive agencies
    async def get_inactive_agencies(self, session: AsyncSession):
        query = (
            select(Agency)
            .where(Agency.is_activated == False)
            .order_by(desc(Agency.created_at))
            # .join(Report, Agency.uid == Report.agency_uid)
            # .join(Follow_Up_Reports, Report.uid == Follow_Up_Reports.report_uid)
            # .options(
            #     joinedload(Agency.reports),
            #     joinedload(Agency.reports).joinedload(Report.follow_up_reports),
            # )
        )

        results = await session.exec(query)

        agencies = results.all()

        if not agencies:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "No inactive agency")

        return all_agencies(agencies)

    # create agency
    async def create_agency(
        self, agency_data: AgencyCreateModel, session: AsyncSession
    ):
        query = select(Agency).where(
            func.lower(agency_data.email) == func.lower(Agency.email)
        )

        result = await session.exec(query)

        agency_exist = result.unique().one_or_none()

        if agency_exist:
            raise InvalidException(
                status.HTTP_406_NOT_ACCEPTABLE, "Email already taken"
            )

        new_agency = Agency(
            uid=uuid.uuid4(),
            agency_name=agency_data.agency_name,
            email=agency_data.email,
            phone=agency_data.phone_number,
            is_activated=False,
            password_hash=pwd_context.hash(agency_data.password),
        )

        session.add(new_agency)

        await session.commit()

        return "Registration successful"

    # activate/deactivate agency
    async def toggle_agency_status(
        self, agency_id: uuid.UUID, status: bool, session: AsyncSession
    ) -> str:
        query = select(Agency).where(Agency.uid == agency_id)

        result = await session.exec(query)

        response = result.one_or_none()

        if not response:
            return NotFoundException(status.HTTP_404_NOT_FOUND, "Agency not found")

        response.is_activated = status

        session.add(response)
        await session.commit()

        return "Agency activated" if status else "Agency deactivated"

    # update agency details
    async def update_agency(
        self,
        agency_id: uuid.UUID,
        agency_data: AgencyUpdateModel,
        session: AsyncSession,
    ):
        query = select(Agency).where(Agency.uid == agency_id)

        result = await session.exec(query)

        agencies = result.unique().all()

        if not agencies:
            return NotFoundException(status.HTTP_404_NOT_FOUND, "Agency not found")

        agency = next((a for a in agencies if a.uid == agency_id), None)

        if not agency:
            return NotFoundException(status.HTTP_404_NOT_FOUND, "Agency not found")

        agency.agency_name = agency_data.agency_name
        agency.email = agency_data.email
        agency.phone = agency_data.phone_number

        session.add(agency)

        await session.commit()

        return status.HTTP_200_OK

    # agency login
    async def agency_login(self, model: AgencyLoginModel, session: AsyncSession) -> str:
        agency_data = model.model_dump()

        hashed_password = pwd_context.hash(agency_data["password"])

        query = select(Agency).where(
            Agency.email
            == agency_data["email"] & Agency.password_hash
            == hashed_password
        )

        result = await session.exec(query)

        agency = result.one_or_none()

        if agency:
            return "You've been logged in"

        raise NotFoundException(
            status.HTTP_404_NOT_FOUND,
            f"No agency with this email ({agency_data["email"]}) found",
        )

    async def update_report_status(
        self, report_id: str, status: AgencyReportUpdateModel, session: AsyncSession
    ) -> str:
        reports = await ReportService.get_report(report_id, session)

        for report in reports:
            report.progress = status

        session.add_all(reports)

        await session.commit()

        return "Report has been updated successfully"
