#!/usr/bin/python3
"""Function definition that reads txt file and prints to std out """


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as fp:
        print(fp.read(), end="")
