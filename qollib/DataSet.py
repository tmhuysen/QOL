import numpy as np
import sys

from qollib.stringmethods import newlined_tabbed_data_string_to_dataset


class ConstrainedData:

    def __init__(self, data):
        self.data = self.__data_init__(data)

    def __data_init__(self, data):
        if isinstance(data, str):
            return np.asarray(newlined_tabbed_data_string_to_dataset(data, float))
        if isinstance(data, np.ndarray):
            return data
        if isinstance(data, list) or isinstance(data, tuple):
            return np.asarray(data)
        else:
            try:
                return newlined_tabbed_data_string_to_dataset(data.read(), float)
            except Exception:
                print("unsupported data type:", sys.exc_info()[0])
                raise

    # GETTERS
    def get_data(self):
        return self.data

    def get_energy(self, index = None, name = False):
        if name:
            return "Energy (hartree)"

        if index is None:
            return self.get_data()[0]
        else:
            return self.get_data()[0][index]

    def get_lambda(self, index = None, name = False):
        if name:
            return "Chemical Potential"

        if index is None:
            return self.get_data()[1]
        else:
            return self.get_data()[1][index]

    def get_population(self, index = None, name = False):
        if name:
            return "Population (a.u.)"

        if index is None:
            return self.get_data()[2]
        else:
            return self.get_data()[2][index]

    def get_entropy(self, index = None, name = False):
        if name:
            return "Shannon Entropy"
        if index is None:
            return self.get_data()[3]
        else:
            return self.get_data()[3][index]
