#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        mult_ret = len(sentence), sentence[0]
        return mult_ret
    else:
        return None
