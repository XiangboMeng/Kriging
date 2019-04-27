"""
Geometric example
------------------
A small example script showing the usage of the 'geographic' coordinates type
for ordinary kriging on a sphere.
"""

from pykrige.ok import OrdinaryKriging
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from scipy.io import loadmat

X = loadmat("x.mat")
Y = loadmat("y.mat")
Z = loadmat("z.mat")
Z0 = loadmat("Z0.mat")

x = X["x"]
y = Y["y"]
z = Z["z"]

tmp = Z0["Z"]
#plt.imshow(tmp)
#plt.colorbar()
#plt.show()

gridx = np.arange(0, 500, 1)
gridx = gridx.astype(np.float64)
gridy = np.arange(0, 500, 1)
gridy = gridy.astype(np.float64)



# Create ordinary kriging object:
OK = OrdinaryKriging(x, y, z, variogram_model='exponential', verbose=False, enable_plotting=False)

print("working")
# Execute on grid:
z1, ss1 = OK.execute('grid', gridx, gridy)

plt.imshow(z1)
plt.show()

print("finished")
