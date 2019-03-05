import warnings
import numpy as np

from qollib.stringmethods import newlined_tabbed_data_string_to_dataset

print("Imported qollib readers...")


class TsfReader:  # tab separated file reader
    """
    Class that takes converts a tab separated file (@param file_name) and converts each column of that file into list
    """

    def __init__(self, file_name, n_sets = None, data_type = None):
        self.__file_name = file_name
        self.__n_sets = n_sets
        self.__define_type = data_type
        self.data = self.__data_init__()

    """
    Reads the file (@self.__file_name) and stores the data (@self.data)
    """

    def __data_init__(self):
        file = open(self.__file_name, "r")
        data = file.read()
        file.close()
        data_sets = newlined_tabbed_data_string_to_dataset(data, self.__define_type)
        if self.__n_sets is None:
            self.__n_sets = len(data_sets)
        else:
            if len(data_sets) != self.__n_sets:
                warnings.warn("expected number of data sets does not match the data file, %d instead of %d"
                              % (len(data_sets), self.__n_sets))

        return tuple(data_sets)

    # GETTERS
    def number_of_sets(self):
        return self.__n_sets


class ConstrainedReader(TsfReader):
    """
    Reader for specifically Constrained .out files
    """

    def __init__(self, file_name):
        super().__init__(file_name, 4, float)

    # GETTERS
    def get_data(self):
        return np.asarray(super().data)

    def get_energy(self, index = None):
        if index is None:
            return self.get_data()[0]
        else:
            return self.get_data()[0][index]

    def get_lambda(self, index = None):
        if index is None:
            return self.get_data()[1]
        else:
            return self.get_data()[1][index]

    def get_population(self, index = None):
        if index is None:
            return self.get_data()[2]
        else:
            return self.get_data()[2][index]

    def get_entropy(self, index = None):
        if index is None:
            return self.get_data()[3]
        else:
            return self.get_data()[3][index]
