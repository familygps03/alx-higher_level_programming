#!/usr/bin/python3
def complex_delete(input_dict, target_value):
    while target_value in input_dict.values():
        for key, value in input_dict.items():
            if value == target_value:
                del input_dict[key]
                break
    return input_dict
