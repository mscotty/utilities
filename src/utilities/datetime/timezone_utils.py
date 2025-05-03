from datetime import datetime, timezone, timedelta
import pytz
from typing import Optional

def get_utc_now() -> datetime:
    """Returns the current UTC datetime with timezone awareness."""
    return datetime.now(timezone.utc)

def convert_to_timezone(dt: datetime, target_timezone: str) -> Optional[datetime]:
    """
    Converts a datetime object to a specified timezone.

    Args:
        dt: The datetime object to convert. It can be naive (no timezone info) or aware.
            If naive, it is assumed to be in UTC.
        target_timezone: The name of the target timezone (e.g., 'America/New_York', 'Europe/London').
                       Use the `get_all_timezones()` function to see available options.

    Returns:
        A timezone-aware datetime object in the target timezone if successful, otherwise None.
    """
    try:
        tz = pytz.timezone(target_timezone)
        if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
            # If the datetime object is naive, assume it's in UTC and make it aware
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(tz)
    except pytz.exceptions.UnknownTimeZoneError:
        print(f"Error: Unknown timezone '{target_timezone}'.")
        return None

def convert_from_timezone(dt: datetime, source_timezone: str, target_timezone: str) -> Optional[datetime]:
    """
    Converts a datetime object from one timezone to another.

    Args:
        dt: A timezone-aware datetime object in the source timezone.
        source_timezone: The name of the source timezone.
        target_timezone: The name of the target timezone.

    Returns:
        A timezone-aware datetime object in the target timezone if successful, otherwise None.
    """
    try:
        source_tz = pytz.timezone(source_timezone)
        target_tz = pytz.timezone(target_timezone)
        if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
            print(f"Warning: The datetime object is naive. Assuming it's in '{source_timezone}'.")
            dt = source_tz.localize(dt)
        return dt.astimezone(target_tz)
    except pytz.exceptions.UnknownTimeZoneError as e:
        print(f"Error: Unknown timezone: {e}")
        return None

def get_all_timezones() -> list[str]:
    """Returns a sorted list of all available timezone names from pytz."""
    return sorted(pytz.all_timezones)

def get_current_timezone_name() -> str:
    """
    Attempts to get the current local timezone name.
    Note: This might not always be accurate or specific depending on the system.
    """
    try:
        import time
        return time.tzname[time.localtime().tm_isdst]
    except AttributeError:
        return "UTC" # Default if timezone name cannot be determined

def is_timezone_aware(dt: datetime) -> bool:
    """Checks if a datetime object is timezone-aware."""
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None

def is_timezone_naive(dt: datetime) -> bool:
    """Checks if a datetime object is timezone-naive."""
    return dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None

def get_timezone_offset(timezone_name: str, dt: Optional[datetime] = None) -> Optional[timedelta]:
    """
    Gets the UTC offset for a given timezone at a specific datetime.
    If no datetime is provided, it returns the current offset.

    Args:
        timezone_name: The name of the timezone (e.g., 'America/New_York').
        dt: An optional datetime object. If None, the current time is used.

    Returns:
        A timedelta representing the UTC offset, or None if the timezone is unknown.
    """
    try:
        tz = pytz.timezone(timezone_name)
        if dt is None:
            dt_aware = datetime.now(tz)
        elif dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
            dt_aware = tz.localize(dt)
        else:
            dt_aware = dt.astimezone(tz)
        return dt_aware.utcoffset()
    except pytz.exceptions.UnknownTimeZoneError:
        print(f"Error: Unknown timezone '{timezone_name}'.")
        return None

def get_timezone_abbreviation(timezone_name: str, dt: Optional[datetime] = None) -> Optional[str]:
    """
    Gets the timezone abbreviation (e.g., 'EST', 'PST', 'GMT') for a given timezone
    at a specific datetime. If no datetime is provided, it returns the current abbreviation.

    Args:
        timezone_name: The name of the timezone.
        dt: An optional datetime object. If None, the current time is used.

    Returns:
        The timezone abbreviation as a string, or None if the timezone is unknown.
    """
    try:
        tz = pytz.timezone(timezone_name)
        if dt is None:
            dt_aware = datetime.now(tz)
        elif dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
            dt_aware = tz.localize(dt)
        else:
            dt_aware = dt.astimezone(tz)
        return dt_aware.strftime('%Z')
    except pytz.exceptions.UnknownTimeZoneError:
        print(f"Error: Unknown timezone '{timezone_name}'.")
        return None
    
def create_fixed_timezone(offset_hours: int, offset_minutes: int = 0, name: Optional[str] = None) -> timezone:
    """
    Creates a fixed-offset timezone object.

    Args:
        offset_hours: The offset from UTC in hours.
        offset_minutes: The additional offset from UTC in minutes (default is 0).
        name: An optional name for the timezone.

    Returns:
        A timezone object with the specified fixed offset.
    """
    offset = timedelta(hours=offset_hours, minutes=offset_minutes)
    return timezone(offset, name=name)

# Example Usage (can be removed or put in a separate test file)
if __name__ == "__main__":
    utc_now = get_utc_now()
    print(f"Current UTC time: {utc_now}")

    ny_timezone = "America/New_York"
    london_timezone = "Europe/London"

    ny_time = convert_to_timezone(utc_now, ny_timezone)
    print(f"Current New York time: {ny_time}")

    london_time = convert_to_timezone(utc_now, london_timezone)
    print(f"Current London time: {london_time}")

    # Example of converting between timezones
    if ny_time and london_time:
        london_time_from_ny = convert_from_timezone(ny_time, ny_timezone, london_timezone)
        print(f"London time converted from New York time: {london_time_from_ny}")

    all_tzs = get_all_timezones()
    print(f"\nNumber of available timezones: {len(all_tzs)}")
    print(f"First 10 timezones: {all_tzs[:10]}")

    naive_dt = datetime.now()
    aware_dt = get_utc_now()
    print(f"\nIs naive_dt aware? {is_timezone_aware(naive_dt)}")
    print(f"Is aware_dt aware? {is_timezone_aware(aware_dt)}")
    print(f"Is naive_dt naive? {is_timezone_naive(naive_dt)}")
    print(f"Is aware_dt naive? {is_timezone_naive(aware_dt)}")

    current_tz_name = get_current_timezone_name()
    print(f"\nCurrent local timezone name (approximate): {current_tz_name}")