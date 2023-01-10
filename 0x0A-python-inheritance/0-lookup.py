#!/usr/bin/python3

""" 
This module returns a list of all available attributes and method of an object
"""

def lookup(obj):
    """This function will return the list as specified in the above doc"""
    return dir(obj)
