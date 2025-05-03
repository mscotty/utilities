import os
import portalocker  # You might need to install this: pip install portalocker
from typing import IO

class FileLock:
    """A simple context manager for file locking."""
    def __init__(self, filepath: str, timeout: float = None):
        self.filepath = filepath
        self.timeout = timeout
        self._file = None

    def acquire(self, flags: int = portalocker.LOCK_EX | portalocker.LOCK_NB) -> None:
        """Acquire the lock."""
        self._file = open(self.filepath, 'r+')
        portalocker.lock(self._file, flags, timeout=self.timeout)

    def release(self) -> None:
        """Release the lock."""
        if self._file:
            portalocker.unlock(self._file)
            self._file.close()
            self._file = None

    def __enter__(self) -> IO:
        """Enter the context."""
        self.acquire()
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context."""
        self.release()

# Example usage:
# with FileLock("my_resource.lock"):
#     # Access the protected resource
#     with open("data.txt", "a") as f:
#         f.write("Data updated\n")