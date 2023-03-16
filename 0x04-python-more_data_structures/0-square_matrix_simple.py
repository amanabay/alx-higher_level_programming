#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_matrix = [[cell ** 2 for cell in row] for row in matrix]
    return sq_matrix
