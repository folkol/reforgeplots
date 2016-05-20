from numpy import loadtxt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open('points.dat') as f:
    data = f.read()

xs, ys = data.split('|')

print xs, ys

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
Axes3D.plot_wireframe(xs, ys, zs, *args, **kwargs)
