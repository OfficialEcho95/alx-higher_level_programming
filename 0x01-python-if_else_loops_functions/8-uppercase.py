#!/usr/bin/python3

def uppercase(str):
    for m in str:
        if ord(m) >=97 and ord(m) <=122:
            str = chr(ord(m)-32)
            print("{}".format(str))
