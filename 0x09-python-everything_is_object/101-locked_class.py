#!/usr/bin/python3
"""
A class that prevents the user from dynamically creating a new instance except if the new instance attribute is called first_name
"""
class LockedClass:
    """ The LockedClass """

    __slots__ = ['first_name']
