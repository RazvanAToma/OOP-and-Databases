# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    print(my_list[11])
except IndexError:
    print("Specified Index is out of range...")