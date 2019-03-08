import unittest
import numpy as np

from config import libpath
from qollib.stringmethods import array_to_csl, newlined_tabbed_data_string_to_dataset


class TestStringMethods(unittest.TestCase):

    def test_array_to_csl(self):
        array1 = ["a", "e", "i", "m", "q", "u", "y"]
        array2 = ["b", "f", "j", "n", "r", "v", "z"]
        array3 = np.arange(0, 10, 1)

        self.assertEqual(array_to_csl(array1), "a,e,i,m,q,u,y")
        self.assertEqual(array_to_csl(array2), "b,f,j,n,r,v,z")
        self.assertEqual(array_to_csl(array3), "0,1,2,3,4,5,6,7,8,9")

    def test_newlined_tabbed_data_string_to_dataset(self):
        file = open(libpath("tests/data/tsf_data"), "r")
        data = newlined_tabbed_data_string_to_dataset(file.read())

        column0 = ["a", "e", "i", "m", "q", "u", "y"]
        column1 = ["b", "f", "j", "n", "r", "v", "z"]
        column2 = ["c", "g", "k", "o", "s", "w", "1"]
        column3 = ["d", "h", "l", "p", "t", "x", "2"]

        self.assertEqual(column0, data[0])
        self.assertEqual(column1, data[1])
        self.assertEqual(column2, data[2])
        self.assertEqual(column3, data[3])

        file.close()


if __name__ == '__main__':
    unittest.main()
