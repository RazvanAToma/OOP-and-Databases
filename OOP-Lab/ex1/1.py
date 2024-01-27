

# Define a class named Computation
class Computation():

    # Define the constructor (__init__) for the class
    def __init__(self) -> None:
        pass


    # Define a method named add to perform addition
    def add(self, num1, num2):
        return num1 + num2


    # Define a method named subtract to perform subtraction
    def subtract(self, num1, num2):
        return num1 - num2


    # Define a method named multiply to perform multiplication
    def multiply(self, num1, num2):
        return num1 * num2


    # Define a method named divide to perform division
    def divide(self, num1, num2):
        # Check if the divisor is not zero before performing division
        if num2 != 0:
            return num1 / num2
        else:
            return("Cannot divide by zero")

# Create an instance of the Computation class
computation_instance = Computation()

# Call the add method of the Computation instance with arguments 5 and 5
result_addition = computation_instance.add(5, 5)

# Print the result of the addition
print(result_addition)

