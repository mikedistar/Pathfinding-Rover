# Rover pathfinding algorithim by Jonathan and Michael

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import LinearLocator

fig = plt.figure()

ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# Make data.
x = np.arange(-5, 5, 0.1)
xlen = len(x)
y = np.arange(-5, 5, 0.1)
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
surf = ax1.plot_surface(X, Y, Z, rstride=3, cstride=3, cmap="viridis", linewidth=0, alpha=0.5, axlim_clip=True)

# Customize the z axis.
ax1.set_zlim(-5, 5)
ax1.zaxis.set_major_locator(LinearLocator(6))

ax1.plot(x, x, np.sin(x) + np.cos(x), "--", color="red", linewidth=3, axlim_clip=True)

ax2.imshow(Z, interpolation="bilinear", extent=(-5,5,-5,5))
ax2.contour(X, Y, Z, colors="black")
ax2.plot(x,x, "--", color="red", linewidth=3)

plt.show()
