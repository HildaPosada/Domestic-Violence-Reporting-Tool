from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from fastapi import status
from src.auth.models import User
from src.report.models import Report, Follow_Up_Reports
from src.report.schemas import (
    ReportCreateModel,
    ReportUpdateModel,
    Follow_Up_Create_Model,
)
from sqlalchemy.orm import joinedload
from src.utils import custom_uuid
from src.utils.map import all_reports, all_follow_ups
from src.auth.service import UserService
from src.exception_handler.global_exception import NotFoundException, InvalidException
import uuid
from src.report.enums import ReportProgress
from sqlalchemy.sql.expression import func


class ReportService:
    async def get_all_user_reports(self, username: str, session: AsyncSession):
        if username.lower() == "anonymous":
            raise InvalidException(
                status.HTTP_406_NOT_ACCEPTABLE, "Cannot get reports for anonymous user"
            )

        query = (
            select(Report)
            .where(func.lower(Report.username) == func.lower(username))
            .options(joinedload(Report.follow_up_reports))
            .order_by(desc(Report.created_at))
        )

        result = await session.exec(query)
        response = result.unique().all()

        if not response:
            raise NotFoundException(
                status.HTTP_404_NOT_FOUND, "No report found for user"
            )

        return all_reports(response)

    async def get_all_reports(self, session: AsyncSession):
        query = (
            select(Report)
            .where(Report.is_active)
            .options(joinedload(Report.follow_up_reports))
        )
        result = await session.exec(query)
        response = result.unique().all()

        if not response:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "No reports available")

        return all_reports(response)

    async def get_report(self, report_id: uuid.UUID, session: AsyncSession):
        query = (
            select(Report)
            .where(Report.uid == report_id, Report.is_active)
            .options(joinedload(Report.follow_up_reports))
        )
        result = await session.exec(query)
        report = result.unique().one_or_none()

        if not report:
            raise NotFoundException(
                status.HTTP_404_NOT_FOUND, f"Report with id ({report_id}) not found"
            )

        return all_reports([report])

    async def create_report(
        self, model: ReportCreateModel, session: AsyncSession
    ) -> str:
        try:
            report_id = str(custom_uuid.short_id())  # Generate unique ID
            new_report = Report(
                uid=report_id,
                username=model.username,
                description=model.description,
                agency_uid=model.agency_id,
                is_active=True,
                progress=ReportProgress.Submitted,
            )

            session.add(new_report)
            await session.commit()

            return report_id
        except Exception as ex:
            await session.rollback()
            print(f"Exception at {ex}")
            raise

    async def update_report(
        self,
        username: str,
        report_id: str,
        model: ReportUpdateModel,
        session: AsyncSession,
    ):

        query = select(Report).where(func.lower(Report.username) == func.lower(username), Report.is_active)

        user = await session.exec(query)

        user_reports = user.unique().all()

        if not user_reports:
            raise NotFoundException(
                status.HTTP_404_NOT_FOUND, "User not found or no active report"
            )

        report = next((r for r in user_reports if r.uid == report_id), None)

        if not report:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "Report not found")

        report.description = model.description
        report.agency_uid = model.agency_id

        session.add(report)
        await session.commit()

        return status.HTTP_200_OK

    async def add_follow_up(
        self, report_id: str, model: Follow_Up_Create_Model, session: AsyncSession
    ):
        report = await self.get_report(report_id, session)
        if report:
            follow_up = Follow_Up_Reports(
                description=model.description, report_id=report_id, is_active=True
            )
            session.add(follow_up)
            await session.commit()
            return status.HTTP_201_CREATED
        else:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "Report not found")

    async def get_all_follow_ups(self, report_id: str, session: AsyncSession):
        query = select(Follow_Up_Reports).where(
            Follow_Up_Reports.report_uid == report_id, Follow_Up_Reports.is_active
        )
        result = await session.exec(query)
        response = result.all()

        if not response:
            raise NotFoundException(
                status.HTTP_404_NOT_FOUND, "No follow-up reports found"
            )

        return all_follow_ups(response)
