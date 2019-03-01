# -*- coding: utf-8 -*-
import subprocess

class Executable1D:
    """
    This class wraps an executable and its input in a class
     the executable should only hx@ave one option you would like to vary the input for
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
    def create_exe(self, varied_inputs):
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
    run the defined executable assuming the varied arguments are set
    """
    def run(self):
        if len(self.__args) < 3 :
            raise Exception("NON-VALID EXECUTABLE")
        subprocess.run(self.__args)

    """
    runs the defined executable after updating the exe arguments with @param varied_inputs
     
     @param varied_inputs               input (string) related to the @member varied_option
    """
    def run(self, varied_inputs):
        self.set_arguments(varied_inputs)
        self.run()

    # SETTERS
    def set_arguments(self, varied_inputs):
        self.__args = self.create_exe(varied_inputs)

