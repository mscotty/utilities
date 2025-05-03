from bs4 import BeautifulSoup  # You might need to install this: pip install beautifulsoup4
from typing import List, Optional

def extract_text_from_html(html_content: str) -> str:
    """Extracts all text content from HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator=' ', strip=True)

def find_all_links(html_content: str, base_url: Optional[str] = None) -> List[str]:
    """Finds all 'href' attributes in 'a' tags in HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    if base_url:
        from urllib.parse import urljoin
        return [urljoin(base_url, link) for link in links]
    return links

# More advanced HTML parsing would involve more specific selectors and attribute extraction.