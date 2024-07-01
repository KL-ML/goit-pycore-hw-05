"""A function that identifies all float numbers in the text and returns a generator."""
import re

def generator_numbers(text: str):
    """identifies all float numbers in the text.

    Args:
        text (str): a string of text in which float numbers are written without errors, 
        clearly separated by spaces on both sides.

    Yields:
        float: a float number, a separate word, two decimal places
    """

    pattern = r"\b\d+\.\d{2}\b"
    for item in re.findall(pattern, text, re.IGNORECASE):
        yield float(item)
