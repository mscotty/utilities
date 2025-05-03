from datetime import datetime, timedelta

def create_interval(start_time: datetime, end_time: datetime) -> tuple[datetime, datetime]:
    """Creates a time interval tuple, ensuring start_time <= end_time."""
    if start_time <= end_time:
        return (start_time, end_time)
    else:
        return (end_time, start_time)

def is_datetime_within_interval(dt: datetime, interval: tuple[datetime, datetime]) -> bool:
    """Checks if a datetime object falls within a given interval (inclusive)."""
    start, end = interval
    return start <= dt <= end

def get_interval_duration(interval: tuple[datetime, datetime]) -> timedelta:
    """Calculates the duration of a time interval."""
    start, end = interval
    return end - start