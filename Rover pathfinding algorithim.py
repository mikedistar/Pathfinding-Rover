# Rover pathfinding algorithim by Jonathan and Michael

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import LinearLocator

ax = plt.figure().add_subplot(111, projection='3d')

# Make data.
x = np.arange(-5, 5, 0.25)
xlen = len(x)
y = np.arange(-5, 5, 0.25)
ylen = len(y)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

# Create an empty array of strings with the same shape as the meshgrid, and
# populate it with two colors in a checkerboard pattern.
'''colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
'''

# Plot the surface with face colors taken from the array we made.
surf = ax.plot_surface(X, Y, Z, color='b', linewidth=0)

#ax.contour3D(X, Y, Z, cmap="coolwarm")

# Customize the z axis.
ax.set_zlim(-5, 5)
ax.zaxis.set_major_locator(LinearLocator(6))

ax.plot(x, x, np.sin(x) + np.cos(x), "--k", color="red", linewidth=3)

plt.show()
