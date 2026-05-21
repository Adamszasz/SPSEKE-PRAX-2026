from datetime import datetime


def round_to_whole_hour(dt: datetime) -> datetime:
    return dt.replace(minute=0, second=0, microsecond=0)