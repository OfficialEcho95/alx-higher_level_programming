#!/usr/bin/python3

def max_integer(my_list=[]):
    myMax = my_list[0]

    if len(my_list) == 0:
        return "None"

    for num in my_list:
        if myMax < num:
            myMax = num
    return (myMax)
