import filecmp

def are_files_equal(file1: str, file2: str, shallow: bool = True) -> bool:
    """
    Compares two files to check if they are equal.

    Args:
        file1: Path to the first file.
        file2: Path to the second file.
        shallow: If True, only the stat signatures (size, mtime, etc.) are compared.
                 If False, a byte-by-byte comparison is performed.

    Returns:
        True if the files are equal, False otherwise.
    """
    return filecmp.cmp(file1, file2, shallow=shallow)