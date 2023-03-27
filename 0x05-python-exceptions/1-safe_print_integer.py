#!/usr/bin/python3

def safe_print_integer(value):
    """ Prints an integer with "{:d}".format()
    Args:
        value (int): int to be printed
    Returns:
        True if no TypeError or ValueError has occured
        False if not
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
