# Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n.
# Test this method.

class factorial_sum():

    def __init__(self) -> None:
        pass

    def Sum(self, num):
        numbers_to_add = []

        while num != 0:
            numbers_to_add.append(num)
            num -= 1
        
        return sum(numbers_to_add)
    


factorial_sum_instance = factorial_sum()

print(factorial_sum_instance.Sum(10))