#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    cop_list = my_list.copy()

    if idx < 0:
        return cop_list
    elif idx > len(my_list) - 1:
        return cop_list

    cop_list[idx] = element
    return cop_list
