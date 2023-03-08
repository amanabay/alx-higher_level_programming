#!/usr/bin/python3

def uppercase(str):
    upper = ''
    for letter in str:
        if ord(letter) >= 65:
            upper += chr(ord(letter) - 32)
    return upper
