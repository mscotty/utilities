import gzip
import os
from typing import Optional

def compress_gzip(input_filepath: str, output_filepath: Optional[str] = None, compresslevel: int = 9) -> str:
    """
    Compresses a file using gzip.

    Args:
        input_filepath: The path to the file to compress.
        output_filepath: The path to the output .gz file. If None, it defaults to input_filepath + '.gz'.
        compresslevel: The compression level (0-9, with 9 being the highest).

    Returns:
        The path to the created .gz file.
    """
    if output_filepath is None:
        output_filepath = input_filepath + '.gz'
    with open(input_filepath, 'rb') as f_in, gzip.open(output_filepath, 'wb', compresslevel=compresslevel) as f_out:
        f_out.writelines(f_in)
    return output_filepath

def decompress_gzip(gzip_filepath: str, output_filepath: Optional[str] = None) -> str:
    """
    Decompresses a .gz file.

    Args:
        gzip_filepath: The path to the .gz file.
        output_filepath: The path to the decompressed output file. If None, it defaults to the input_filepath without the '.gz' extension.

    Returns:
        The path to the created decompressed file.
    """
    if output_filepath is None and gzip_filepath.endswith('.gz'):
        output_filepath = gzip_filepath[:-3]
    elif output_filepath is None:
        raise ValueError("Output filepath must be provided if input filepath does not end with '.gz'")

    with gzip.open(gzip_filepath, 'rb') as f_in, open(output_filepath, 'wb') as f_out:
        f_out.writelines(f_in)
    return output_filepath