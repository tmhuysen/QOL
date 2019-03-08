import subprocess

from qollib.DataSet import ConstrainedData

print("Imported qollib executable1D...")


class Executable1D:
    """
    This class wraps an executable and its input in a class
     the executable should only have one option you would like to vary the input for
    """

    def __init__(self, path, static_options, static_inputs, varied_option, return_data = False, name = None,
                 name_flag = "-e"):
        self.__path = path
        self.__static_options = static_options
        self.__static_inputs = static_inputs
        self.__varied_option = varied_option
        self.__varied_input = None
        self.__n_options = len(static_options)
        self.__args = tuple()
        self.return_data = return_data
        self.__name = name
        self.__name_flag = name_flag

    """ 
    creates a runnable argument for an executable
     
     @param varied_inputs               input (string) related to the @member varied_option
    """

    def __create_exe__(self):
        arg_list = list()
        arg_list.append(self.__path)
        for i in range(self.__n_options):
            arg_list.append(self.__static_options[i])
            arg_list.append(self.__static_inputs[i])
        arg_list.append(self.__varied_option)
        arg_list.append(self.__varied_input)

        if self.__name is not None:
            arg_list.append(self.__name_flag)
            arg_list.append(self.__name)
        self.__args = tuple(arg_list)

    """
    runs the defined executable, if input is given update the exe arguments with @param varied_inputs

     @param varied_inputs               input (string) related to the @member varied_option
    """

    def run(self, varied_inputs = None):
        if varied_inputs is not None:
            self.set_arguments(varied_inputs)
        if len(self.__args) < 3:
            raise Exception("NON VALID 1D-EXECUTABLE")
        if self.return_data:
            return subprocess.check_output(self.__args, universal_newlines = True)
        else:
            subprocess.run(self.__args)

    # SETTERS
    def set_arguments(self, varied_inputs):
        self.__varied_input = varied_inputs
        self.__create_exe__()

    def set_name(self, name):
        self.__name = name
        self.__create_exe__()


    def get_args(self):
        return self.__args


class ConstrainedExeWrapper:
    """
    Wrapper around Executable1D for data handling class

    """

    def __init__(self, exe1d):
        self.__exe1d = exe1d

        # Wrapper relies on exe output test if flag is set to true
        if not isinstance(exe1d, Executable1D):
            raise Exception("only instantiate with Executable1D class")
        elif not exe1d.return_data:
            raise Exception("return data flag is off")

    def __find_basis(self):
        print(self.__exe1d.__args)
        for index, element in enumerate(self.__exe1d.__args, 0):
            if element == "-s":
                return self.__exe1d.__args(index + 1)

    def run(self, varied_inputs = None):
        return ConstrainedData(self.__exe1d.run(varied_inputs))

    def set_name(self, name):
        self.__exe1d.set_name(name)
