import requests
from typing import Optional, Dict, Any

def http_get(url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, str]] = None, timeout: int = 10) -> Optional[requests.Response]:
    """Performs an HTTP GET request."""
    try:
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP GET error for {url}: {e}")
        return None

def http_post(url: str, headers: Optional[Dict[str, str]] = None, data: Optional[Any] = None, json: Optional[Any] = None, timeout: int = 10) -> Optional[requests.Response]:
    """Performs an HTTP POST request."""
    try:
        response = requests.post(url, headers=headers, data=data, json=json, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP POST error for {url}: {e}")
        return None

def get_response_json(response: requests.Response) -> Optional[Dict]:
    """Parses the JSON response from an HTTP request."""
    if response and response.headers.get('Content-Type', '').startswith('application/json'):
        try:
            return response.json()
        except ValueError:
            print("Error decoding JSON response.")
            return None
    return None

def get_response_text(response: requests.Response) -> Optional[str]:
    """Gets the text content of an HTTP response."""
    return response.text if response else None

# Example usage (requires 'requests' library: pip install requests):
# response = http_get("https://api.example.com/data", params={"id": 1})
# if response:
#     data = get_response_json(response)
#     if data:
#         print(data)