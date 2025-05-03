from typing import List, Dict, Any

def print_table(data: List[Dict[str, Any]], headers: List[str] = None, padding: int = 2) -> None:
    """Prints a list of dictionaries as a formatted table."""
    if not data:
        print("No data to display.")
        return

    if headers is None:
        headers = list(data[0].keys())

    column_widths = {header: len(header) for header in headers}
    for row in data:
        for header, value in row.items():
            column_widths[header] = max(column_widths[header], len(str(value)))

    # Print header
    header_row = " | ".join(header.ljust(column_widths[header]) for header in headers)
    print(header_row)
    print("-" * len(header_row))

    # Print data rows
    for row in data:
        row_values = [str(row.get(header, '')).ljust(column_widths[header]) for header in headers]
        print(" | ".join(row_values))

# Example usage:
# my_data = [
#     {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
#     {"Name": "Charlie", "Age": 32, "City": "Chicago"},
#     {"Name": "David", "Age": 28, "City": "Houston"},
# ]
# print_table(my_data)
# print("\nWith custom headers:")
# print_table(my_data, headers=["Employee Name", "Years", "Location"])