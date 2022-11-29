#!/usr/bin/python3

def uppercase(str):
    for m in str:
        if ord(str) >=97 and ord(str) <=122:
            str = chr(ord(m))
            print("{}".format(str))
