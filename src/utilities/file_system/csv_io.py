import csv
from typing import List, Dict, TextIO

def read_csv_file(filepath: str, delimiter: str = ',', quotechar: str = '"') -> List[List[str]]:
    """Reads a CSV file and returns the data as a list of lists."""
    data = []
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in reader:
            data.append(row)
    return data

def write_csv_file(filepath: str, data: List[List[str]], delimiter: str = ',', quotechar: str = '"') -> None:
    """Writes data (list of lists) to a CSV file."""
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter, quotechar=quotechar)
        writer.writerows(data)

def read_csv_file_as_dicts(filepath: str, delimiter: str = ',', quotechar: str = '"') -> List[Dict[str, str]]:
    """Reads a CSV file and returns the data as a list of dictionaries (using the header row as keys)."""
    data = []
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in reader:
            data.append(row)
    return data

def write_csv_file_from_dicts(filepath: str, data: List[Dict[str, str]], fieldnames: List[str],
                             delimiter: str = ',', quotechar: str = '"') -> None:
    """Writes a list of dictionaries to a CSV file."""
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter, quotechar=quotechar)
        writer.writeheader()
        writer.writerows(data)