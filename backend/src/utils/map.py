from src.report.schemas import ReportResponseModel
from src.report.schemas import Follow_Up_Response_Model

def all_reports(reports):
    response_models = [
        ReportResponseModel(
            report_id=report.uid,
            description=report.description,
            agency_id=report.agency_uid,
            date_created=report.created_at,
            follow_ups=all_follow_ups(report.follow_ups)
        )
        for report in reports
    ]
    return response_models


def all_follow_ups(follow_ups):
    response_model = [
        Follow_Up_Response_Model(
            follow_up_id=follow_up.uid,
            description=follow_up.description,
            report_id=follow_up.report_id,
            date_created=follow_up.created_at
        )
        for follow_up in follow_ups
    ]
    return response_model


