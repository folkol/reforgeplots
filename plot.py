from numpy import loadtxt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
xs, yx, zs, dps = loadtxt('data.csv', delimiter=',', skiprows=1, usecols=(0,1,2), unpack=True)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
Axes3D.plot_wireframe(xs, ys, zs, *args, **kwargs)

