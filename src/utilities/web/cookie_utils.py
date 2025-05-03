from http.cookies import SimpleCookie
from typing import Dict, Optional

def parse_cookies(cookie_string: str) -> Dict[str, str]:
    """Parses a cookie string into a dictionary of name-value pairs."""
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    return {key: morsel.value for key, morsel in cookie.items()}

def format_cookies(cookies: Dict[str, str]) -> str:
    """Formats a dictionary of cookies into a cookie string."""
    cookie = SimpleCookie()
    for key, value in cookies.items():
        cookie[key] = value
    return cookie.output(header='')

# Example usage:
# cookie_str = "name=value; sessionid=12345; expires=Wed, 21 Oct 2025 07:28:00 GMT"
# parsed_cookies = parse_cookies(cookie_str)
# print(parsed_cookies)
# formatted_cookies = format_cookies({"lang": "en", "theme": "dark"})
# print(formatted_cookies)