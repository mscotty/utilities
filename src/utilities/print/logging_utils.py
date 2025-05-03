import logging
import datetime
import os
from typing import Optional

# Define custom log levels if needed
LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}

DEFAULT_LOG_FORMAT = '%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def setup_logger(name: str, log_file: Optional[str] = None, level: str = 'INFO',
                 formatter: logging.Formatter = None, date_formatter: str = DEFAULT_DATE_FORMAT) -> logging.Logger:
    """
    Sets up a logger with specified configurations.

    Args:
        name: The name of the logger.
        log_file: Optional path to a log file. If None, logs will only go to the console.
        level: The logging level (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
        formatter: Optional logging.Formatter object. If None, a default formatter is used.
        date_formatter: The format string for the date/time in the logs.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVELS.get(level.upper(), logging.INFO))

    if formatter is None:
        formatter = logging.Formatter(DEFAULT_LOG_FORMAT, datefmt=date_formatter)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Create file handler if log_file is provided
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

# You can create pre-configured loggers for different parts of your application
def get_app_logger(name: str, log_file: Optional[str] = 'app.log', level: str = 'INFO') -> logging.Logger:
    """Gets a pre-configured logger for the main application."""
    return setup_logger(name, log_file=log_file, level=level)

def get_utils_logger(name: str, log_file: Optional[str] = 'utils.log', level: str = 'DEBUG') -> logging.Logger:
    """Gets a pre-configured logger for utility functions."""
    return setup_logger(name, log_file=log_file, level=level)

# Example Usage (can be removed or put in a separate test file)
if __name__ == "__main__":
    app_logger = get_app_logger(__name__)
    utils_logger = get_utils_logger("my_utils")

    app_logger.info("Application started.")
    utils_logger.debug("Debugging a utility function.")

    try:
        result = 10 / 0
    except ZeroDivisionError:
        app_logger.error("Division by zero error!", exc_info=True)

    app_logger.warning("Low disk space detected.")
    utils_logger.info("Utility function completed successfully.")
    app_logger.critical("Critical system failure!")