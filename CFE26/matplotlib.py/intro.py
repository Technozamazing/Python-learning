# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
import matplotlib.pyplot as plt

# Parabola function plot:
x = list(range(-1000, 1000))
y = [x**2 for x in x]


plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()