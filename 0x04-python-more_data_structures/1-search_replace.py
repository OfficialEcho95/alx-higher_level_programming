#!/usr/bin/python3

def search_replace(my_list, search, replace):
    hold = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            hold.append(replace)
        hold.append(my_list[i])
    return hold
