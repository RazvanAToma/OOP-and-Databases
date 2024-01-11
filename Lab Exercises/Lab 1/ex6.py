# Write a NumPy program to split a given text into lines and split the single line into array values.

import numpy as np

# Option 1
my_array = np.array("Opp Gave 6")

my_array = np.char.split(my_array, " ")

print(my_array)


# Option 2

# Define the text
text = "This is a sample text to be split into lines and array values."

# Split the text into lines
lines = text.split("\n")
print(lines)

# Split each line into array values
array_values = []
for line in lines:
    array_values.append(line.split(" "))

# Convert the list of lists to a NumPy array
array = np.array(array_values)

# Print the array
print(array)
