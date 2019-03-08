import numpy as np
from scipy.interpolate import interp1d


# def interpolate(min_bound, max_bound, exe, access_data_method, access_data_set_method, threshold, iterations):
from qollib.stringmethods import array_to_csl


class IterativeInterpolator:
    def __init__(self, max_bound, min_bound, exe, access_target, access_input):
        self.max = max_bound
        self.min = min_bound
        self.exe = exe
        # self.access_data_method = access_data_method
        self.access_target = access_target
        self.access_input = access_input

    def interpolateIteratively(self, interval, threshold, max_iterations, start_set):


        interpolated_input = start_set
        converged = False
        iterations = 0
        while not converged:
            data = self.__run__(interpolated_input)
            fit = interp1d(self.access_target(data), self.access_input(data))
            requested_values = np.arange(self.access_target(data)[0], self.access_target(data)[-1], interval)

            if self.__approx__(requested_values, self.access_target(data), threshold):
                converged = True
            interpolated_input = fit(requested_values)

            if iterations >= max_iterations:
                converged = True
            iterations += 1
        return interpolated_input

    @staticmethod
    def __approx__(set1, set2, threshold):
        if len(set1) != len(set2):
            return False

        for i in range(len(set1)):
            if abs(set1[i] - set2[i]) > threshold:
                return False
        return True

    def __run__(self, input_set):

        if input_set[0] != self.min:
            input_set = np.insert(input_set, 0, self.min)
        if input_set[-1] != self.max:
            input_set = np.append(input_set,self.max)
        print(input_set)
        return self.exe.run(array_to_csl(input_set))
