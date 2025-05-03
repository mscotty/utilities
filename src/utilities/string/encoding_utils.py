from typing import Optional

def encode_to_bytes(text: str, encoding: str = 'utf-8', errors: str = 'strict') -> bytes:
    """Encodes a string to bytes using the specified encoding."""
    return text.encode(encoding, errors)

def decode_from_bytes(data: bytes, encoding: str = 'utf-8', errors: str = 'strict') -> str:
    """Decodes bytes to a string using the specified encoding."""
    return data.decode(encoding, errors)

# You could add functions for base64 encoding/decoding here as well if needed.
import base64

def encode_to_base64(text: str) -> str:
    """Encodes a string to Base64."""
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')

def decode_from_base64(base64_string: str) -> str:
    """Decodes a Base64 string."""
    base64_bytes = base64_string.encode('utf-8')
    text_bytes = base64.b64decode(base64_bytes)
    return text_bytes.decode('utf-8')