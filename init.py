import pathlib

def libpath(path):
    return pathlib.Path((pathlib.Path(__file__).parent.resolve()),path)