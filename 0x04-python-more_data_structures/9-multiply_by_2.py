#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    mul_2d = {}

    for i in a_dictionary:
        mul_2d[i] = a_dictionary[i] * 2

    return mul_2d
