from typing import Dict

def parse_headers(header_string: str) -> Dict[str, str]:
    """Parses a string of HTTP headers into a dictionary."""
    headers = {}
    for line in header_string.strip().splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
    return headers

def format_headers(headers: Dict[str, str]) -> str:
    """Formats a dictionary of HTTP headers into a string."""
    return '\n'.join(f"{key}: {value}" for key, value in headers.items())

# Example usage:
# header_str = "Content-Type: application/json\nUser-Agent: MyBot/1.0\nAccept-Language: en-US,en;q=0.9"
# parsed = parse_headers(header_str)
# print(parsed)
# formatted = format_headers({"X-Custom-Header": "value", "Cache-Control": "no-cache"})
# print(formatted)