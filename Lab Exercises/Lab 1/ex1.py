# Write a Python program to sum all the items in a list.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Option 1
my_sum = 0

for number in my_list:
    my_sum += number

print(my_sum)


# Option 2
also_my_sum = sum(my_list)

print(also_my_sum)