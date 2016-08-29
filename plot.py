from numpy import loadtxt
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open('points.dat') as f:
    xs = f.readline().split(',')
    ys = f.readline().split(',')
    dps = (int(x, 16) for x in f.readline().split('|'))

print xs, ys, dps

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = numpy.meshgrid(xs, ys)
Axes3D.plot_wireframe(X, Y)
