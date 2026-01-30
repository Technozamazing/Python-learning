# Subplots let you draw multiple plots in one figure.
# subplot() --> return tuple of two entities(objects)
# print(plt.subplots(1, 2))
# Fig object --> Canvas
# 2D array of Axes(numpy array) object


# Figure = The entire canvas
# Axes = A single plot(subplot)

# Parabola function plot:
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

x = np.array(range(-1000, 1000))
y = [x**2 for x in x]
ax[0, 0].plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
ax[0, 0].set_title('Parabolic Function')

ax[0, 1].plot([1, 2, 3], [1, 2, 3])
plt.xlabel('x axis')
plt.ylabel('y axis')
ax[0, 1].set_title("y = x")

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x)
ax[1, 0].set_title('Sine Function')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
ax[1, 0].plot(x, y)

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.cos(x)
ax[1, 1].set_title('Cosine Function')
ax[1, 1].plot(x, y)

plt.show()