import pathlib

""" method to ensure that the absolute path is found

@param path                 relative string or path object

@return absolute path
"""


def libpath(path):
    return pathlib.Path((pathlib.Path(__file__).parent.resolve()), path)
