# Create a method called testPrim() in the Calculation class to test the primality of a given integer.
# Test this method.

class Calculation():

    def __init__(self) -> None:
        pass

    def testPrim(self, num):

        if num == 1:
            return f"{num} is NOT a prime number"
        elif num == 2:
            return f"{num} IS a prime number"
        elif num > 1:
            for i in range (2, num):
                if (num % i) == 0:
                    return f"{num} is NOT a prime number"
                else:
                    return f"{num} IS a prime number"
        


calculation_instance = Calculation()

print(calculation_instance.testPrim(2))