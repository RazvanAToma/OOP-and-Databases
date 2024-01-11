# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    userIntInput = int(input("Type a number: \n"))
except ValueError:
    print("Please input a valid integer")