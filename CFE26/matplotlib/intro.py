# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias
import matplotlib.pyplot as plt


# Parabola function plot:
import numpy as np
x = np.array(range(-1000, 1000))
y = [x**2 for x in x]
plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Parabolic function')
plt.show()



# Sine function plot:
import numpy as np
x = np.linspace(-2*np.pi, 2*np.pi, 1000)        # range = [-2π, 2π]  -- This range is divided into 1000 equal parts.
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Sine function')
print(x)
plt.show()