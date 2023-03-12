#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = ()

    atuple = tuple_a + (0, 0)
    btuple = tuple_b + (0, 0)

    tuple_sum = atuple[0] + btuple[0], atuple[1] + btuple[1]
    return tuple_sum
