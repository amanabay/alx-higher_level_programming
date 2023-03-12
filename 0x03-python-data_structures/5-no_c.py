#!/usr/bin/python3

def no_c(my_string):
    no_c_string = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ''
        no_c_string += i

    return no_c_string
