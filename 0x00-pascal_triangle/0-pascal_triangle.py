#!/usr/bin/python3
""" This module contains a pascals triangle function """


def pascal_triangle(n):
    """
        returns a list of lists of integers reprsenting
        the Pascal's triangle of n
    """

    triangle_list = []

    if n >= 1:
        triangle_list.append([1])
    if n >= 2:
        triangle_list.append([1, 1])

    if not n > 2:
        return triangle_list

    for i in range(2, n):
        new_tri = [1]
        prev_tri = triangle_list[i - 1]
        for j in range(0, len(prev_tri) - 1):
            new_tri.append(prev_tri[j] + prev_tri[j + 1])
        new_tri.append(1)
        triangle_list.append(new_tri)

    return triangle_list
