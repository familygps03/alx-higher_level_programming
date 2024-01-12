#!/usr/bin/python3

def multiply_values_by_2(input_dictionary):
    modified_dictionary = input_dictionary.copy()

    for key, value in list(modified_dictionary.items()):
        modified_dictionary[key] = value * 2

    return modified_dictionary
