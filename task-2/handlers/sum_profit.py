"""Calculates the total amount of float numbers from generator."""
from typing import Callable

def sum_profit(text: str, func: Callable):
    """The function calculates the total of float numbers in the input string.

    Args:
        text (str): a string of text in which float numbers are written without errors, clearly separated by spaces on both sides.
        func (Callable): A generator function that iterates over all float numbers in the text.

    Returns:
        float: the total amount
    """
    total = 0
    for salary in func(text):
        total += salary
    return total
