# Write a Python program to combine two dictionaries by adding values for common keys.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 4, 'b': 5, 'd': 6}

def combine_dicts(dict1, dict2):
    combined_dict = {}

    for key, value in dict1.items():
        combined_dict[key] = value

    for key, value in dict2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value
            
    return combined_dict

combined_dict = combine_dicts(dict1, dict2)
print(combined_dict)