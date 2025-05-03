from urllib.parse import urlparse, urlunparse, urljoin, quote, unquote
from typing import Optional

def parse_url(url: str) -> tuple:
    """Parses a URL into its components."""
    parsed = urlparse(url)
    return parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, parsed.fragment

def build_url(scheme: str, netloc: str, path: str, params: str = '', query: str = '', fragment: str = '') -> str:
    """Builds a URL from its components."""
    return urlunparse((scheme, netloc, path, params, query, fragment))

def join_url_paths(base: str, url: str) -> str:
    """Joins a base URL with another URL."""
    return urljoin(base, url)

def url_encode(text: str, encoding: str = 'utf-8') -> str:
    """URL-encodes a string."""
    return quote(text, encoding=encoding)

def url_decode(encoded_text: str, encoding: str = 'utf-8') -> str:
    """URL-decodes a string."""
    return unquote(encoded_text, encoding=encoding)

def get_domain_from_url(url: str) -> Optional[str]:
    """Extracts the domain (netloc) from a URL."""
    parsed = urlparse(url)
    return parsed.netloc if parsed.netloc else None

# Example usage:
# url = "https://www.example.com:8080/path?query=string#fragment"
# scheme, netloc, path, _, query, fragment = parse_url(url)
# print(f"Scheme: {scheme}, Netloc: {netloc}, Path: {path}, Query: {query}, Fragment: {fragment}")
# new_url = build_url("http", "anothersite.org", "/page", query="id=123")
# print(f"New URL: {new_url}")