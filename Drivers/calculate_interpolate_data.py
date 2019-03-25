import numpy as np

from qollib.DataSet import ConstrainedData
from qollib.executable import Executable1D, ConstrainedExeWrapper
from qollib.graphing import ConstrainedGrapher
from qollib.interpolation import IterativeInterpolator

#path = "/Users/quantum/CLionProjects/forks/gqcp/build/drivers/c_constrained_N_O"
path = "/Users/quantum/PycharmProjects/QOL/personalgen/exes/c_constrained_N_O"
exe = Executable1D(path, ["-d", "-s", "-n"], ["10.0", "STO-3G", "true"], "-c", True, name = "naturals")

constrained_exe = ConstrainedExeWrapper(exe)

minb = -5.0
maxb = 5.0
x = np.arange(minb, maxb, 0.01)

modulels = IterativeInterpolator(maxb, minb, constrained_exe, ConstrainedData.get_population,
                                 ConstrainedData.get_lambda)

modulels.interpolateIteratively(0.01, 0.01, 5, x)
