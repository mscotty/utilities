import time
from typing import Optional

def print_progress_bar(iteration: int, total: int, prefix: str = '', suffix: str = '', decimals: int = 1, length: int = 50, fill: str = '█') -> None:
    """
    Prints a progress bar to the console.

    Args:
        iteration: Current iteration number (int).
        total: Total number of iterations (int).
        prefix: Prefix string (str, optional).
        suffix: Suffix string (str, optional).
        decimals: Positive number of decimals in percent complete (int, optional).
        length: Character length of bar (int, optional).
        fill: Bar fill character (str, optional).
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()

# Example usage:
# items = list(range(0, 100))
# for i, item in enumerate(items):
#     time.sleep(0.05)
#     print_progress_bar(i + 1, len(items), prefix='Progress:', suffix='Complete', length=50)