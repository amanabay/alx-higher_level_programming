#!/usr/bin/python3

def safe_print_division(a, b):
    """ Divides 2 integers and prints the resultself.

        a (int): divisor
        b (int): dividend

        Return: a divided by b
    """

    try:
        c = a / b
    except (ZeroDivisionError, TypeError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c
