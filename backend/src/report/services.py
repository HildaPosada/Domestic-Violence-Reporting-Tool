from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from fastapi import status
from src.auth.models import User
from src.report.models import Report, Follow_Up_Reports
from src.report.schemas import ReportCreateModel, Follow_Up_Create_Model
from sqlalchemy.orm import joinedload
from src.utils import custom_uuid
from src.utils.map import all_reports, all_follow_ups
from src.auth.service import UserService
from src.exception_handler.global_exception import NotFoundException
import uuid


class ReportService:
    async def get_all_user_reports(self, username: str, session: AsyncSession):
        query = select(Report).join(User).where(User.username == username).options(
            joinedload(Report.user), joinedload(Report.follow_up_reports)
        ).order_by(desc(Report.created_at))

        result = await session.exec(query)
        response = result.all()

        if not response:
            raise NotFoundException(status.HTTP_404_NOT_FOUND,  "No report found for user")
        
        return all_reports(response)

    async def get_all_reports(self, session: AsyncSession):
        query = select(Report).where(Report.is_active).options(joinedload(Report.follow_up_reports))
        result = await session.exec(query)
        response = result.all()

        if not response:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "No reports available")
        
        return all_reports(response)

    async def get_report(self, report_id: uuid.UUID, session: AsyncSession):
        query = select(Report).where(Report.uid == report_id, Report.is_active).options(joinedload(Report.follow_up_reports))
        result = await session.exec(query)
        report = result.first()

        if not report:
            raise NotFoundException(status.HTTP_404_NOT_FOUND,  f"Report with id ({report_id}) not found")
        
        return all_reports([report])

    async def create_report(self, user_uid: str | None, model: ReportCreateModel, session: AsyncSession) -> str:
        report_id = custom_uuid.short_id  # Generate unique ID
        new_report = Report(
            uid=report_id,
            description=model.description,
            agency_uid=model.agency_id,
            user_uid=user_uid,
            is_active=True,
        )

        session.add(new_report)
        await session.commit()

        return report_id

    async def update_report(self, user_id: str, report_id: str, model: ReportCreateModel, session: AsyncSession):
        user = await UserService.get_user_by_id(user_id, session)
        if not user:
            raise NotFoundException(status.HTTP_404_NOT_FOUND,  "User not found")

        query = select(Report).where(Report.uid == report_id, Report.is_active)
        result = await session.exec(query)
        report = result.one_or_none()

        if not report:
            raise NotFoundException(status.HTTP_404_NOT_FOUND,  "Report not found")

        report.description = model.description
        report.agency_uid = model.agency_id

        session.add(report)
        await session.commit()

        return status.HTTP_200_OK

    async def add_follow_up(self, report_id: str, model: Follow_Up_Create_Model, session: AsyncSession):
        report = await self.get_report(report_id, session)
        if report:
            follow_up = Follow_Up_Reports(
                description=model.description,
                report_id=report_id,
                is_active=True
            )
            session.add(follow_up)
            await session.commit()
            return status.HTTP_201_CREATED
        else:
            raise NotFoundException(status.HTTP_404_NOT_FOUND,  "Report not found")

    async def get_all_follow_ups(self, report_id: str, session: AsyncSession):
        query = select(Follow_Up_Reports).where(Follow_Up_Reports.report_uid == report_id, Follow_Up_Reports.is_active)
        result = await session.exec(query)
        response = result.all()

        if not response:
            raise NotFoundException(status.HTTP_404_NOT_FOUND, "No follow-up reports found")
        
        return all_follow_ups(response)
