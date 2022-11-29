#!/usr/bin/python3

def uppercase(str):
    for m in range(65, 91):
        if ord(str) >=97 and ord(str) <=122:
            new_string += chr(ord(m)-32)
        else:
            new_string += m
    print("{}".format(new_string))
