#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return "None"
    for k, v in a_dictionary.items():
        m = max(v)
        if m:
            print(k)
