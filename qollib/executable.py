import subprocess

print("Imported qollib executable1D...")


class Executable1D:
    """
    This class wraps an executable and its input in a class
     the executable should only have one option you would like to vary the input for
    """

    def __init__(self, path, static_options, static_inputs, varied_option, varied_index):
        self.__path = path
        self.__static_options = static_options
        self.__static_inputs = static_inputs
        self.__varied_option = varied_option
        self.__varied_index = varied_index
        self.__n_options = len(static_options) + 1
        self.__args = tuple()

    """ 
    creates a runnable argument for an executable
     
     @param varied_inputs               input (string) related to the @member varied_option
    """

    def __create_exe__(self, varied_inputs):
        arg_list = list()
        for i in range(self.__n_options):
            if i == self.__varied_index:
                arg_list.append(self.__varied_option)
                arg_list.append(varied_inputs)
                arg_list.append(self.__static_options[i])
                arg_list.append(self.__static_inputs[i])
            else:
                arg_list.append(self.__static_options[i])
                arg_list.append(self.__static_inputs[i])
        return arg_list

    """
    runs the defined executable, if input is given update the exe arguments with @param varied_inputs

     @param varied_inputs               input (string) related to the @member varied_option
    """

    def run(self, varied_inputs = None):
        if varied_inputs is not None:
            self.set_arguments(varied_inputs)
        if len(self.__args) < 3:
            raise Exception("NON VALID 1D-EXECUTABLE")
        subprocess.run(self.__args)

    # SETTERS
    def set_arguments(self, varied_inputs):
        self.__args = self.__create_exe__(varied_inputs)
