import locale
from datetime import datetime
from typing import Optional

def format_datetime_localized(dt: datetime, format_string: str, locale_name: str) -> Optional[str]:
    """
    Formats a datetime object according to a format string and a specified locale.

    Args:
        dt: The datetime object to format.
        format_string: The format string (as used with strftime).
        locale_name: The name of the locale to use (e.g., 'en_US.UTF-8', 'de_DE').
                     Make sure the locale is installed on your system.

    Returns:
        The formatted datetime string if successful, otherwise None.
    """
    try:
        original_locale = locale.getlocale()
        locale.setlocale(locale.LC_TIME, locale_name)
        formatted_string = dt.strftime(format_string)
        locale.setlocale(locale.LC_TIME, original_locale)  # Restore original locale
        return formatted_string
    except locale.Error:
        print(f"Error: Locale '{locale_name}' not supported or installed.")
        return None
    except TypeError:
        print("Error: Invalid datetime object or format string.")
        return None

def get_supported_locales() -> list[str]:
    """
    Returns a list of supported locale names on the system.
    Note: The availability of locales depends on the operating system.
    """
    supported = []
    for name in locale.locale_alias:
        try:
            locale.setlocale(locale.LC_TIME, name)
            supported.append(name)
        except locale.Error:
            pass
    locale.setlocale(locale.LC_TIME, '') # Reset to the default locale
    return sorted(list(set(supported)))

# Example Usage (can be removed or put in a separate test file)
if __name__ == "__main__":
    now = datetime.now()
    format_str = "%A, %B %d, %Y - %I:%M %p"

    us_locale = "en_US.UTF-8"
    de_locale = "de_DE" # You might need to adjust this based on your system's installed locales

    formatted_us = format_datetime_localized(now, format_str, us_locale)
    print(f"Formatted ({us_locale}): {formatted_us}")

    formatted_de = format_datetime_localized(now, format_str, de_locale)
    print(f"Formatted ({de_locale}): {formatted_de}")

    supported_locales = get_supported_locales()
    print("\nSupported Locales:")
    for loc in supported_locales[:10]: # Print first 10 for brevity
        print(f"- {loc}")
    print(f"... (and {len(supported_locales) - 10} more)")