#!/usr/bin/python3
def convert_to_uppercase(char):
    return chr(ord(char) - 32) 
	if 'a' <= char <= 'z' 
	else char
def uppercase(input_str):
    result_str = ""
    for character in input_str:
        result_str += convert_to_uppercase(character)
    print(result_str)
