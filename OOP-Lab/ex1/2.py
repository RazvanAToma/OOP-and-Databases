# Create a method called Factorial() which allows to calculate the factorial of an integer.
# Test the method by instantiating the class.

import numpy as np

class factorial():

    def __init__(self) -> None:
        pass

    def factorial(self, num):
        factorial_numbers = []

        while num != 0:
            factorial_numbers.append(num)
            num -= 1

        num_factorial = np.prod(factorial_numbers)

        return num_factorial


factorial_instance = factorial()

print(factorial_instance.factorial(10))