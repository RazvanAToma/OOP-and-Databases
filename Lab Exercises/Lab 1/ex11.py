# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    int1 = int(input("First Number:"))
    int2 = int(input("Second Number:"))
    print(int(int1/int2))
except ZeroDivisionError:
    print("You cannot divide by zero...")