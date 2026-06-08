import functools


class CacheDecorator:
    """Клас-декоратор для кешування результатів методів"""

    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        # Створюємо ключ з аргументів
        cache_key = self._make_key(args, kwargs)

        if cache_key in self.cache:
            print(f"[CACHE HIT] Returning cached result for {self.func.__name__}{cache_key}")
            return self.cache[cache_key]

        print(f"[CACHE MISS] Computing result for {self.func.__name__}{cache_key}")
        result = self.func(*args, **kwargs)
        self.cache[cache_key] = result
        return result

    def _make_key(self, args, kwargs):
        """Створює ключ для кешу з аргументів"""
        # Конвертуємо kwargs в tuple для хешування
        kwargs_tuple = tuple(sorted(kwargs.items()))
        return (args, kwargs_tuple)

    def __get__(self, instance, owner):
        """Дескриптор для підтримки методів класу"""
        if instance is None:
            return self
        return functools.partial(self.__call__, instance)


# Приклад використання
class Calculator:
    """Клас калькулятора з кешованими методами"""

    @CacheDecorator
    def fibonacci(self, n):
        """Обчислює n-те число Фібоначчі (рекурсивно)"""
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    @CacheDecorator
    def power(self, base, exponent):
        """Піднесення до степеня"""
        print(f"  -> Calculating {base}^{exponent}")
        return base ** exponent

    @CacheDecorator
    def factorial(self, n):
        """Обчислює факторіал"""
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)


class MathOperations:
    """Клас з математичними операціями"""

    @CacheDecorator
    def sum_range(self, start, end):
        """Сума чисел у діапазоні"""
        print(f"  -> Computing sum from {start} to {end}")
        return sum(range(start, end + 1))

    @CacheDecorator
    def multiply(self, a, b, c=1):
        """Множення з опціональним третім параметром"""
        print(f"  -> Computing {a} * {b} * {c}")
        return a * b * c


if __name__ == "__main__":
    print("=== Тестування кешування методів ===\n")

    calc = Calculator()

    print("--- Fibonacci ---")
    print(f"fibonacci(5) = {calc.fibonacci(5)}")
    print(f"fibonacci(5) = {calc.fibonacci(5)}")
    print(f"fibonacci(7) = {calc.fibonacci(7)}")

    print("\n--- Power ---")
    print(f"power(2, 3) = {calc.power(2, 3)}")
    print(f"power(2, 3) = {calc.power(2, 3)}")
    print(f"power(3, 2) = {calc.power(3, 2)}")
    print(f"power(2, 3) = {calc.power(2, 3)}")

    print("\n--- Factorial ---")
    print(f"factorial(5) = {calc.factorial(5)}")
    print(f"factorial(5) = {calc.factorial(5)}")
    print(f"factorial(6) = {calc.factorial(6)}")

    print("\n=== Тестування з kwargs ===\n")
    math_ops = MathOperations()

    print("--- Sum Range ---")
    print(f"sum_range(1, 10) = {math_ops.sum_range(1, 10)}")
    print(f"sum_range(1, 10) = {math_ops.sum_range(1, 10)}")

    print("\n--- Multiply with kwargs ---")
    print(f"multiply(2, 3) = {math_ops.multiply(2, 3)}")
    print(f"multiply(2, 3) = {math_ops.multiply(2, 3)}")
    print(f"multiply(2, 3, c=4) = {math_ops.multiply(2, 3, c=4)}")
    print(f"multiply(2, 3, c=4) = {math_ops.multiply(2, 3, c=4)}")
    print(f"multiply(2, 3) = {math_ops.multiply(2, 3)}")
