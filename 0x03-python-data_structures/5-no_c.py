#!/usr/bin/python3

def no_c(my_string):
    no_c_string = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ''
        no_c_string += i

    return no_c_string


stri = 'The cat carried the laod ad Clsass WAs Casd Cassie'
print(no_c(stri))
