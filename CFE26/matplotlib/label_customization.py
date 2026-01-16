# Customizing labels -- like Fontsize, Fontfamily, Fontweight, FontColor, Alignment of the label, can be customize

import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/LOQ/OneDrive/Desktop/students_marks_extended.csv")
df = df.drop_duplicates()
df = df.fillna({'Physics': 32, 'Mathematics': 32})
font1 = {'family': 'serif', 'color': 'blue', 'size': 17}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 13}

x = df['SN']
y = df['Mathematics']
plt.plot(x, y, color = "#0065CA", marker='o', linestyle='solid', ms=2, label='Mathematics')
plt.plot(df['SN'], df['Physics'], color = "#009726", marker='o', linestyle='solid', ms=2, label='Physics')
plt.title('Marks of 25 Students in Phy & Math', fontdict=font1)
plt.xlabel('Students by Roll', font2)
plt.ylabel('Marks Obtained by Students', font2)
plt.grid(True)
plt.tick_params('both', colors='darkred')
plt.xticks(df['SN'])
plt.legend(
    loc='upper left',
    bbox_to_anchor=(1, 1),
    fontsize=12
)


plt.show()

