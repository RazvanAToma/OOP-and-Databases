# Write a Python program to return all keys that share the same values in a given dictionary.

my_dict = {'a': 1, 'b': 3, 'c': 2, 'd': 1, 'e': 3}

def same_values(dict):
    for key, value in dict.items():
        val = dict[key]
        

same_values(my_dict)