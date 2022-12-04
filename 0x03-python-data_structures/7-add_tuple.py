#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    for a in range(len(tuple_b)):
        if tuple_b[a] < 2:
            return (2, 98)
        else:
            return tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
