# As we have seen about Line plots  --  which are used to show trend over time.
# Bar Charts  --  are used to show the comparision btn two quantities.

import numpy as np
import matplotlib.pyplot as plt

x = ['BEI', 'BCT', 'BGE', 'BCE', 'BEL', 'BAM', 'BME']
y = np.array([48, 48, 26, 112, 33, 8, 44])

plt.title('Students by Faculty')
plt.bar(x, y, zorder=3)
# plt.barh(x, y, zorder=3)
plt.yticks(range(1, 113, 5))
plt.grid(axis='y', zorder=0)
plt.xlabel('Faculty')
plt.ylabel('Students Admitted')
plt.show()