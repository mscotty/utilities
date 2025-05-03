import os

def get_current_working_directory() -> str:
    """Returns the current working directory."""
    return os.getcwd()

def change_current_working_directory(path: str) -> None:
    """Changes the current working directory."""
    os.chdir(path)

def get_user_home_directory() -> str:
    """Returns the user's home directory."""
    return os.path.expanduser("~")