# Write a Python program to combine two dictionaries by adding values for common keys.

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

kilefructecumparateluni = {'mere': 1, 'pere': 2, 'bananer': 3}
kilefructecumparatevineri = {'mere': 4, 'pere': 5}

combined_dict = combine_dicts(kilefructecumparateluni, kilefructecumparatevineri)
print(combined_dict)