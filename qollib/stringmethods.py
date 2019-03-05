"""
Transform a list of elements to a comma separated line
    eg. [1, 2, 3, 4] becomes:
        1,2,3,4
"""


def array_to_csl(array):
    s = ''.join([str(el) + "," for el in array])
    return s[:-1]
