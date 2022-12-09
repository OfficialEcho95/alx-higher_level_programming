#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    for i in a_dictionary:
        if i not in a_dictionary:
            a_dictionary
    return a_dictionary
