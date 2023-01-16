#!/usr/bin/python3

'''
a script that adds all arguments to a Python list, and then save them to a file
'''
import json
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

arguments = []

filename = "add_item.json"

try:
    arguments = load_from_json_file(filename)
except FileNotFoundError:
    arguments = []

for item in sys.argv[1:]:
    arguments.append(item)

save_to_json_file(arguments, filename)
