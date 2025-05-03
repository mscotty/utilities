import pprint
from typing import Any

def pretty_print(data: Any, indent: int = 2, sort_dicts: bool = True) -> None:
    """Prints Python data structures in a more human-readable format."""
    pp = pprint.PrettyPrinter(indent=indent, sort_dicts=sort_dicts)
    pp.pprint(data)

def pformat_data(data: Any, indent: int = 2, sort_dicts: bool = True) -> str:
    """Formats Python data structures into a pretty-printed string."""
    pp = pprint.PrettyPrinter(indent=indent, sort_dicts=sort_dicts)
    return pp.pformat(data)

# Example usage:
# my_data = {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "hiking"]}
# pretty_print(my_data)
# formatted_data = pformat_data(my_data)
# print(f"Formatted data:\n{formatted_data}")