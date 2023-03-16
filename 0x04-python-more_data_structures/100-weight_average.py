#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    avg = 0
    num = 0

    for t in my_list:
        avg += t[0] * t[1]
        num += t[1]

    return float(avg / num)
