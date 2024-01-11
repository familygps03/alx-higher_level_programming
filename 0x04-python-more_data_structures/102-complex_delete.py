#!/usr/bin/python3
def complex_delete(input_dict, target_value):
    for key, value in sorted(input_dict.items()):
        if value == target_value:
            del input_dict[key]
    return input_dict
