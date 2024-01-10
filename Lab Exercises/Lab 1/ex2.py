# Write a Python program to get the largest number from a list.

my_list = [10, 2, 3, 4, 5, 6, 7, 8, 9]

# Option 1
largest_number = 0

for number in my_list:
    if number > largest_number:
        largest_number = number

print(largest_number)

# Option 2
my_list.sort()

print(my_list[-1])