import re
from typing import List
from typing import Optional

def extract_words(text: str) -> List[str]:
    """Extracts words from a string, removing punctuation and converting to lowercase."""
    return re.findall(r'\b\w+\b', text.lower())

def normalize_text(text: str) -> str:
    """Lowercases and removes leading/trailing whitespace from a string."""
    return text.lower().strip()

def remove_stopwords(words: List[str], stopwords: Optional[set[str]] = None) -> List[str]:
    """Removes common stopwords from a list of words."""
    if stopwords is None:
        stopwords = set(['the', 'a', 'an', 'is', 'are', 'was', 'were', 'of', 'in', 'on', 'at'])
    return [word for word in words if word not in stopwords]

# More advanced NLP tasks would typically involve dedicated libraries like NLTK or SpaCy.