#!/usr/bin/python3

def uniq_add(my_list=[]):
    the_sum = 0
    a_list = set(my_list)
    a_list = list(a_list)
    for i in range(len(a_list)):
        the_sum += a_list[i]
    return the_sum
