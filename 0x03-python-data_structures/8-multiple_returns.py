#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        mult_ret = len(sentence), sentence[0]
        return mult_ret
