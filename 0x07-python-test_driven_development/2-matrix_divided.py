#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list[list[int/float]]): The matrix to divide.
        div (int/float): The number to divide the matrix by.

    Returns:
        list[list[float]]: A list of lists containing the divided matrix.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If sublists are not of the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats.")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
                            integers/floats.")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats.")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
