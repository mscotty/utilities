from datetime import datetime, timedelta
from typing import Union

def add_timedelta(dt: datetime, delta: timedelta) -> datetime:
    """Adds a timedelta to a datetime object."""
    return dt + delta

def subtract_timedelta(dt: datetime, delta: timedelta) -> datetime:
    """Subtracts a timedelta from a datetime object."""
    return dt - delta

def get_time_difference(dt1: datetime, dt2: datetime) -> timedelta:
    """Calculates the difference between two datetime objects."""
    return dt1 - dt2

def add_days(dt: datetime, days: int) -> datetime:
    """Adds a specified number of days to a datetime object."""
    return dt + timedelta(days=days)

def subtract_days(dt: datetime, days: int) -> datetime:
    """Subtracts a specified number of days from a datetime object."""
    return dt - timedelta(days=days)

def add_weeks(dt: datetime, weeks: int) -> datetime:
    """Adds a specified number of weeks to a datetime object."""
    return dt + timedelta(weeks=weeks)

def subtract_weeks(dt: datetime, weeks: int) -> datetime:
    """Subtracts a specified number of weeks from a datetime object."""
    return dt - timedelta(weeks=weeks)

def add_hours(dt: datetime, hours: int) -> datetime:
    """Adds a specified number of hours to a datetime object."""
    return dt + timedelta(hours=hours)

def subtract_hours(dt: datetime, hours: int) -> datetime:
    """Subtracts a specified number of hours from a datetime object."""
    return dt - timedelta(hours=hours)

def add_minutes(dt: datetime, minutes: int) -> datetime:
    """Adds a specified number of minutes to a datetime object."""
    return dt + timedelta(minutes=minutes)

def subtract_minutes(dt: datetime, minutes: int) -> datetime:
    """Subtracts a specified number of minutes from a datetime object."""
    return dt - timedelta(minutes=minutes)

def add_seconds(dt: datetime, seconds: int) -> datetime:
    """Adds a specified number of seconds to a datetime object."""
    return dt + timedelta(seconds=seconds)

def subtract_seconds(dt: datetime, seconds: int) -> datetime:
    """Subtracts a specified number of seconds from a datetime object."""
    return dt - timedelta(seconds=seconds)

def add_months(dt: datetime, months: int) -> datetime:
    """Adds a specified number of months to a datetime object."""
    new_month = (dt.month + months - 1) % 12 + 1
    new_year = dt.year + (dt.month + months - 1) // 12
    try:
        return dt.replace(year=new_year, month=new_month)
    except ValueError:
        # Handle cases where the day of the month is invalid for the new month
        import calendar
        return dt.replace(year=new_year, month=new_month, day=calendar.monthrange(new_year, new_month)[1])

def subtract_months(dt: datetime, months: int) -> datetime:
    """Subtracts a specified number of months from a datetime object."""
    new_month = (dt.month - months - 1) % 12 + 1
    new_year = dt.year + (dt.month - months - 1) // 12
    try:
        return dt.replace(year=new_year, month=new_month)
    except ValueError:
        import calendar
        return dt.replace(year=new_year, month=new_month, day=calendar.monthrange(new_year, new_month)[1])

def add_years(dt: datetime, years: int) -> datetime:
    """Adds a specified number of years to a datetime object."""
    new_year = dt.year + years
    try:
        return dt.replace(year=new_year)
    except ValueError:
        # Handle leap year issues if the original date was Feb 29th
        return dt.replace(year=new_year, month=2, day=28)

def subtract_years(dt: datetime, years: int) -> datetime:
    """Subtracts a specified number of years from a datetime object."""
    new_year = dt.year - years
    try:
        return dt.replace(year=new_year)
    except ValueError:
        return dt.replace(year=new_year, month=2, day=28)

# Example Usage (can be removed or put in a separate test file)
if __name__ == "__main__":
    now = datetime.now()
    print(f"Now: {now}")
    print(f"Add 5 days: {add_days(now, 5)}")
    print(f"Subtract 2 weeks: {subtract_weeks(now, 2)}")
    print(f"Add 3 months: {add_months(now, 3)}")
    print(f"Subtract 1 year: {subtract_years(now, 1)}")

    # Handling edge cases for months
    date_jan_30 = datetime(2025, 1, 30)
    print(f"Adding 1 month to {date_jan_30}: {add_months(date_jan_30, 1)}") # Should go to Feb 28th/29th

    date_feb_29 = datetime(2024, 2, 29) # Leap year
    print(f"Adding 1 year to {date_feb_29}: {add_years(date_feb_29, 1)}") # Should go to Feb 28th