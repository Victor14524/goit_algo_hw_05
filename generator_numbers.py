import re
from typing import Callable


def generator_numbers(text: str) -> float:
    """
    This function generates all real numbers in a given text.

    Args: text (str): The input text to be analyzed.

    Yields: float: Each real number found in the text.
    """
    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', text)
    for num in numbers:
        yield float(num)


def sum_profit(text: str, func: Callable) -> float:
    """
    This function calculates the total sum of all real numbers in a given text.

    Args: text (str): The input text to be analyzed.
          func (Callable): The generator function to extract numbers.

    Returns: float: The total sum of all real numbers.
    """
    total_sum = 0
    for num in func(text):
        total_sum += num
    return total_sum


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,"
        " доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
