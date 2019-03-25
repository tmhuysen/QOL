import numpy as np
import os
import sys
from qollib.DataSet import ConstrainedData
from qollib.executable import Executable1D, ConstrainedExeWrapper
from qollib.interpolation import IterativeInterpolator



exelist = ["constrained_N_O", "c_constrained_N_O"]

distance = sys.argv[1]
exe = int(sys.argv[2])
print(exe)

pathx = os.environ['PEXE1']
path = os.path.join(pathx, exelist[exe])

exe = Executable1D(path, ["-d", "-s"], [str(distance), "STO-3G"], "-c", True, name = "linux")

constrained_exe = ConstrainedExeWrapper(exe)

minb = -5.0
maxb = 5.0
x = np.arange(minb, maxb, 0.01)

modulels = IterativeInterpolator(maxb, minb, constrained_exe, ConstrainedData.get_population,
                                 ConstrainedData.get_lambda)

modulels.interpolateIteratively(0.01, 0.01, 10, x)
