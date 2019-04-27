
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
plt.imshow(tmp)
plt.colorbar()
plt.show()
