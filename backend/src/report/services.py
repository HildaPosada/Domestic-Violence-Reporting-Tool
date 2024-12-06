from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from fastapi.exceptions import HTTPException
from fastapi import status
from src.auth.models import User
from src.report.models import Report, Follow_Up_Reports
from src.report.schemas import ReportCreateModel, Follow_Up_Create_Model
from sqlalchemy.orm import joinedload
from src.utils import custom_uuid
from src.utils.map import all_reports, all_follow_ups
from src.auth.service import UserService
from src.exception_handler.global_exception import NotFoundException


class ReportService:
    # get all reports for user
    async def get_all_user_reports(self, username: str, session: AsyncSession):
        query = select(Report).join(User).where(User.username == username).options(joinedload(Report.user)).options(joinedload(Report.follow_up_reports)).order_by(desc(Report.created_at))

        result = await session.exec(query)

        response = result.all()

        if query is None:
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail=f"No report found for user")

        response_models = all_reports(response)

        return response_models

    # get single report
    async def get_report(self, report_id: str, session: AsyncSession):
        query = select(Report).where(Report.uid == report_id and Report.is_active).options(joinedload(Report.follow_up_reports))

        result = await session.exec(query)

        report = result.first()

        if query is None:
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail=f"Report with id ({report_id}) not found")

        response_model = all_reports([report])

        return response_model

    # create a report
    async def create_report(self, user_uid: str, model: ReportCreateModel, session: AsyncSession):
        user = UserService.get_user_by_id(user_uid, session)

        if user is None:
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail="User not found")

        new_report = Report(
            uid=custom_uuid.short_id,
            description=model.description,
            agency_uid=model.agency_id,
            user_uid=user_uid,
            is_active=True
        )

        session.add(new_report)

        await session.commit()

        return status.HTTP_201_CREATED

    # update report
    async def update_report(self, user_id: str, report_id: str, model: ReportCreateModel, session: AsyncSession):
        user = UserService.get_user_by_id(user_id, session)

        if user is None: 
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail="User not found")

        query = select(Report).where(Report.uid == report_id and Report.is_active)

        result = await session.exec(query)

        if not query:
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail="Report not found")

        report = result.first()

        report.description = model.description
        report.agency_uid = model.agency_id

        session.add(report)

        await session.commit()

        return status.HTTP_200_OK 

    # delete report
    # async def delete_report(self, user_id: str, report_id: str, session: AsyncSession):
    #     user = UserService.get_user_by_id(user_id, session)

    #     if user is None:
    #         return HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")

    #     query = select(Report).where(Report.uid == report_id and Report.is_active)

    #     result = await session.exec(query)

    #     if not query:
    #         return HTTPException(status.HTTP_404_NOT_FOUND, detail="Report not found")

    #     report = result.first()

    #     report.is_active = False

    #     session.add(report)

    #     await session.commit()

    #     return status.HTTP_201_CREATED

    # add additional report
    async def add_follow_up(self, report_id: str, model: Follow_Up_Create_Model, session: AsyncSession):
        report = self.get_report(report_id, session)

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
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail="Report not found")

    async def get_all_follow_ups(self, report_id: str, session: AsyncSession):
        query = select(Follow_Up_Reports).where(Follow_Up_Reports.uid == report_id and Follow_Up_Reports.is_active)

        result = await session.exec(query)

        if not query:
            return NotFoundException(status.HTTP_404_NOT_FOUND, detail="No follow up report found")

        follow_ups = all_follow_ups(result.all())

        return follow_ups
