#!/usr/bin/python3

for alph in range(122, 96, -1):
    if alph % 2 != 0:
        print("{}".format(chr(alph - 32)), end="")
    else:
        print("{}".format(chr(alph)), end="")
