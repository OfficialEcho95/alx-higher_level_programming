#!/usr/bin/python3
'''best score'''

def best_score(a_dictionary):
    if a_dictionary == None:
        return "None"

    return max(a_dictionary, key=a_dictionary.get)
