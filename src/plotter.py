import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

#sample pcolormesh

np.random.seed(19680801)
Z = np.random.rand(10, 10)
x = np.arange(0, 11, 1)  # len = 11
y = np.arange(0, 11, 1)  # len = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)

plt.show()