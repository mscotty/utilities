from datetime import datetime

def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Formats a datetime object into a string."""
    return dt.strftime(fmt)

def parse_datetime(dt_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """Parses a datetime string into a datetime object."""
    return datetime.strptime(dt_str, fmt)

def get_current_timestamp_ms() -> int:
    """Returns the current timestamp in milliseconds."""
    return int(datetime.now().timestamp() * 1000)