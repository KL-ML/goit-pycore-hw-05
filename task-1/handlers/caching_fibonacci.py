""" Calculates the Fibonacci numbers creating and using a cache to store and reuse already calculated values of Fibonacci numbers """

def caching_fibonacci() -> callable:
    """Calculates the Fibonacci numbers creating and using a cache to store and reuse already calculated values of Fibonacci numbers
    
    Raises:
        TypeError: raises an error when parameters in the function are not an integer n < 0

    Returns:
        callable: returns the inner function fibonacci(n) that calculates the Fibonacci number using a cache from an external function
    """

    cache = {}

    def fibonacci(number: int) -> int:

        try:
            if not isinstance(number, int) or number < 0:
                raise TypeError
            if number <= 1:
                return number
            if number in cache:
                return cache[number]
            cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
            return cache[number]

        except TypeError:
            return "Помилка даних: значення параметру повинно бути цілим числом, більшим за нуль"
    return fibonacci
