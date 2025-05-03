from typing import Optional

def are_strings_similar(str1: str, str2: str, threshold: float = 0.8) -> bool:
    """
    Checks if two strings are similar based on a simple character-based similarity.
    Note: For more advanced fuzzy matching, consider libraries like `fuzzywuzzy`.
    """
    if not str1 or not str2:
        return str1 == str2
    longer = str1 if len(str1) > len(str2) else str2
    shorter = str2 if len(str1) > len(str2) else str1
    distance = _levenshtein_distance(longer, shorter)
    similarity = (len(longer) - distance) / len(longer)
    return similarity >= threshold

def _levenshtein_distance(s1: str, s2: str) -> int:
    """Calculates the Levenshtein distance between two strings."""
    if len(s1) < len(s2):
        return _levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# For more robust fuzzy matching, consider using the `fuzzywuzzy` library:
# from fuzzywuzzy import fuzz
# def fuzzy_similarity_ratio(str1: str, str2: str) -> int:
#     return fuzz.ratio(str1, str2)