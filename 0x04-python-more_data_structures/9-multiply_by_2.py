#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return multiplied_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}

result_dict = multiply_by_2(my_dict)

print("Original Dictionary:", my_dict)
print("Multiplied by 2 Dictionary:", result_dict)
