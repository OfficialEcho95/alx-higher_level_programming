#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(i + j for i, j in zip(tuple_a, tuple_a))
    #new_tuple = tuple_a + tuple_a
    #return new_tuple
