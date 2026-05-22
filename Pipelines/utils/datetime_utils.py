from datetime import datetime

def round_to_whole_hour(dt: datetime) -> datetime:
    if not isinstance(dt, datetime):
        raise TypeError(f"Expected datetime object, got {type(dt).__name__} instead")
    return dt.replace(minute=0, second=0, microsecond=0)