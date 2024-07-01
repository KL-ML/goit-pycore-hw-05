"""Use the caching_fibonacci() function to calculate Fibonacci numbers
    """
from handlers import caching_fibonacci

# pylint: disable=not-callable
fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
