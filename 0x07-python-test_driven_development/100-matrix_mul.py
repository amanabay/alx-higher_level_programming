#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """multiplies two matrices

    Args:
        m_a (list of lists of ints/floats): first matrix
        m_b (list of lists of ints/floats): second matrix

    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

        result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result.append(row)
    return result
