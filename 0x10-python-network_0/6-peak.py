#!/usr/bin/python3

"""
    Algorithm that finds peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
        finds the peak in a list of integers

        Args:
            list_of_integers(list (int)): list of integers to find
                                          peak from
    """
    peak = list_of_integers[0]

    for i in list_of_integers:
        if i > peak:
            peak = i

    return peak
