# With our basic plot and graph
# Additionally we can customize it according to our need.

# like for plot(marker):
# marker --> change the icon of marker
# markersize(ms) --> change size of the marker
# markerfacecolor(mfc) --> change the face color of the plot
# markeredgecolor(mec) --> change the edge(joining line) color of the graph


# for line:
# linestyle = ["solid", "dashed", "dotted", "dashdot"],     default = solid
# linewidth = [1, 2, 3, 4, ..],       default = 1
# color = "Any_color", "#value", ..


import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
x2 = np.array([5, 1, 10, 4, 16, 6])
y2 = np.array([1, 5, 4, 10, 6, 16])
marker_style = dict(marker = ".", markersize = 15, markerfacecolor = "#e67c40", markeredgecolor = "#1fc5f9")
line_style = dict(linestyle = "solid", linewidth = 1.5, color = "#1fc5f9")
line_style2 = dict(linestyle = "dashed", linewidth = 2, color = "#2dc070")

plt.plot(x2, y2, **marker_style, **line_style)
plt.plot(x, y, **marker_style, **line_style2)
plt.show()