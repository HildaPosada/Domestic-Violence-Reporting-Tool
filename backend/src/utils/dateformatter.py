from datetime import datetime


def format_date(date):
    dt = datetime.fromisoformat(str(date))

    formatted_date = dt.strftime("%d %b %Y")

    return formatted_date