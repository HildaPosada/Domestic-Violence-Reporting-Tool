from src.report.schemas import ReportResponseModel
from src.report.schemas import Follow_Up_Response_Model
from src.agency.schemas import AgencyResponseModel
from src.utils.dateformatter import format_date

def all_reports(reports):
    response_models = [
        ReportResponseModel(
            user=report.username,
            report_id=report.uid,
            progress=report.progress,
            agency_id=report.agency_uid,
            date_created=format_date(report.created_at),
            follow_ups=all_follow_ups(report.follow_ups) if "follow_ups" in report else None
        )
        # print(report)
        for report in reports
    ]
    return response_models


def all_follow_ups(follow_ups):
    response_model = [
        Follow_Up_Response_Model(
            follow_up_id=follow_up.uid,
            report_id=follow_up.report_id,
            date_created=format_date(follow_up.created_at)
        )
        for follow_up in follow_ups
    ]
    return response_model


def all_agencies(agencies):
    response_model = [
        AgencyResponseModel(
            agency_id=agency.uid,
            agency_name=agency.agency_name,
            email=agency.email,
            phone_number=agency.phone,
            is_activated=agency.is_activated,
            date_created=format_date(agency.created_at),
            reports=all_reports(agency.reports) if "reports" in agency else None
        )
        for agency in agencies
    ]
    return response_model