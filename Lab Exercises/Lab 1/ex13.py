# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    with open("thisFileDoesNotExist.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Could not find specified file...")