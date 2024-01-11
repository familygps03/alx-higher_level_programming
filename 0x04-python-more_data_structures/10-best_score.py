#!/usr/bin/python3
def find_best_score(a_dict):
    if not isinstance(a_dict, dict) or len(a_dict) == 0:
        return None

    result_key = list(a_dict.keys())[0]
    best_score = list(a_dict.values())[0]
    
    for key, value in a_dict.items():
        if value > best_score:
            best_score = value
            result_key = key
            
    return result_key
