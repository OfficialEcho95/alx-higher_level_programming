#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return "None"
    a_max = max(a_dictionary.values())
    return a_max
