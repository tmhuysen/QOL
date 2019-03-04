import unittest
import qollib.readers as readers
from init import libpath


class TestTsfReader(unittest.TestCase):

    def setUp(self):
        self.reader = readers.TsfReader(libpath("tests/data/tsf_data"))

    def tearDown(self):
        pass

    def test_number_of_sets(self):
        self.assertEqual(4, self.reader.number_of_sets())

    def test_data(self):
        column0 = ["a", "e", "i", "m", "q", "u", "y"]
        column1 = ["b", "f", "j", "n", "r", "v", "z"]
        column2 = ["c", "g", "k", "o", "s", "w", "1"]
        column3 = ["d", "h", "l", "p", "t", "x", "2"]

        self.assertEqual(column0, self.reader.data[0])
        self.assertEqual(column1, self.reader.data[1])
        self.assertEqual(column2, self.reader.data[2])
        self.assertEqual(column3, self.reader.data[3])

class TestConstrainedReader(unittest.TestCase):

    def setUp(self):
        self.reader_base = readers.TsfReader(libpath("tests/data/N_O_4_constrained_fci_STO-3G.out"), 4, float)
        self.reader_constrained = readers.ConstrainedReader(libpath("tests/data/N_O_4_constrained_fci_STO-3G.out"))

    def tearDown(self):
        pass

    def test_number_of_sets(self):
        self.assertEqual(self.reader_constrained.number_of_sets(), self.reader_base.number_of_sets())

    def test_data(self):
        self.assertEqual(self.reader_base.data[0], self.reader_constrained.data[0])
        self.assertEqual(self.reader_base.data[1], self.reader_constrained.data[1])
        self.assertEqual(self.reader_base.data[2], self.reader_constrained.data[2])
        self.assertEqual(self.reader_base.data[3], self.reader_constrained.data[3])

if __name__ == '__main__':
    unittest.main()
