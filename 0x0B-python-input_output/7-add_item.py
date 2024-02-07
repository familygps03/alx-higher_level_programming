#!/usr/bin/python3
"""Module for loading, adding, and saving arguments to a Python list."""
from sys import argv
from 6-load_from_json_file import load_from_json_file
from 5-save_to_json_file import save_to_json_file

try:
    json_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    json_list = []

json_list.extend(argv[1:])

save_to_json_file(json_list, 'add_item.json')
