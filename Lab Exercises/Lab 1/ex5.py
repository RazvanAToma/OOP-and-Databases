# Write a NumPy program to create a random 10x4 array and extract the first five rows of the array and store them into a variable.

import numpy as np

# Option 1
my_array = np.arange(0, 40).reshape(10, 4)
first5 = my_array[:5]
print(first5)


# Option 2
arr = np.random.randn(10, 4)
alsoFirst5 = arr[:5]

print(alsoFirst5)