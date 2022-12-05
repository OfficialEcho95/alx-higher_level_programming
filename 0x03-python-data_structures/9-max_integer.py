#!/usr/bin/python3

def max_integer(my_list=[]):
    myMax = my_list[0]

    for num in my_list:
        if my_list == []:
            return "None"
        if myMax < num:
            myMax = num
    return (myMax)
