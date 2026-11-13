# Rover pathfinding algorithim by Jonathan and Michael

import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
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

f = lambda x, y: np.sin(x) + np.cos(y)
Z = f(X,Y)

# Plot the surface with face colors taken from the array we made.
surf = ax1.plot_surface(X, Y, Z, rstride=3, cstride=3, cmap="viridis", linewidth=0, alpha=0.5, axlim_clip=True)

# Customize the z axis.
ax1.set_zlim(-5, 5)
ax1.zaxis.set_major_locator(LinearLocator(6))

# Add contours to the surface plot
ax1.contour(X, Y, Z)

# A test line (replace with the calculated path)
path_line3D, = ax1.plot(x, x, f(x,x), "--", color="red", linewidth=3, axlim_clip=True, zorder=4)

# Create the 2-D contour plot
ax2.imshow(Z, interpolation="bilinear", extent=(-5,5,-5,5))
ax2.contour(X, Y, Z, colors="black")

# Plotting a test line (replace with the calculated path)
path_line2D, = ax2.plot(x,x, "--", color="red", linewidth=3)

# A list of the end points of the pathfinding
#   [0] => Start
#   [1] => End
extrema = [(2,0), (1,1)]

extrema_scatter2D = ax2.scatter([x[0] for x in extrema], [x[1] for x in extrema], facecolors=["red", "blue"], alpha=1)
extrema_scatter3D = ax1.scatter([x[0] for x in extrema], [x[1] for x in extrema], [f(x[0],x[1]) for x in extrema], facecolors=["red", "blue"], alpha=1, zorder=4)

def on_click(event):
    if event.inaxes != ax2:
        return

    if event.button == MouseButton.LEFT:
        # Update start point
        extrema[0] = (event.xdata, event.ydata)
    elif event.button == MouseButton.RIGHT:
        # Update end point
        extrema[1] = (event.xdata, event.ydata)

    xs = [p[0] for p in extrema]
    ys = [p[1] for p in extrema]

    # Update the end points on the plot
    extrema_scatter2D.set_offsets(extrema)
    extrema_scatter3D._offsets3d = (xs, ys, f(xs, ys))

    # Create a list of the points in the path
    path2D = [xs, ys]
    path3D = [xs, ys, f(xs, ys)]

    # Update the line
    path_line2D.set_data(path2D)
    path_line3D.set_data_3d(path3D)
    fig.canvas.draw()

plt.connect("button_press_event", on_click)

plt.show()
