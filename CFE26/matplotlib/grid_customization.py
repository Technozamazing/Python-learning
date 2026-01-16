# We can add and customize the grid using grid() for better readability and Understanding.
# like  --  Selecting axis,  Giving linewidth,  Giving color,  Giving linestyle, etc.

import numpy as np
import matplotlib.pyplot as plt

x = np.array(list(range(0, 6)))
y = np.array(list(range(0, 6)))

plt.plot(x, y)
plt.grid(axis='x', linewidth=2, color='red', linestyle = '-')
plt.grid(axis='y', linewidth=2, color='blue', ls = ':')
# ValueError: '.' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.show()