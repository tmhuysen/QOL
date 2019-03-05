import unittest
import numpy as np

from qollib.stringmethods import array_to_csl


class TestStringMethods(unittest.TestCase):

    def test_array_to_csl(self):
        array1 = ["a", "e", "i", "m", "q", "u", "y"]
        array2 = ["b", "f", "j", "n", "r", "v", "z"]
        array3 = np.arange(0,10,1)

        self.assertEqual(array_to_csl(array1), "a,e,i,m,q,u,y")
        self.assertEqual(array_to_csl(array2), "b,f,j,n,r,v,z")
        self.assertEqual(array_to_csl(array3), "0,1,2,3,4,5,6,7,8,9")


if __name__ == '__main__':
    unittest.main()
