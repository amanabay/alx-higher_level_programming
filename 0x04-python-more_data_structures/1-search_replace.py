#!/usr/bin/python3

def search_replace(my_list, search, replace):
    rep_matrix = []
    for i in range(len(my_list)):
        if (my_list[i] == search):
            rep_matrix.append(replace)
        else:
            rep_matrix.append(my_list[i])

    return rep_matrix
