import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# scatter plot
# hue: allows us to add aditional dimension in seaborn
tips = sns.load_dataset('tips')
print(tips.info())
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.grid(True)
plt.title('Bill Amount vs Tip (On basis of Sex)', family='poppins', weight='medium')
plt.show()



# line plot
data = {
    'day': range(1, 8),
    'hours': [2, 4, 5, 4, 7, 6, 7]
}

sns.lineplot(data=data, x='day', y='hours', marker='o')
plt.title('Studied Hours in a Week')
plt.xlabel('Days')
plt.ylabel('Hours')
plt.grid(True)
plt.show()



# bar plot
sns.barplot(data=tips, x='day', y='tip', errorbar=None)
plt.xlabel('Days')
plt.ylabel('Avarage tips($)')
plt.title('Average Tips by Day of Week')
plt.show()



# count plot
sns.countplot(data=tips, x='sex')
plt.title('Number of Males and Females')
x=tips['sex']
y=tips.count()
# plt.bar(x, y, zorder=3)
plt.grid(axis='y', zorder=0)
plt.show()



# histogram
tips = sns.load_dataset('tips')
sns.histplot(data=tips, x='total_bill', bins=40, kde=True)
plt.title('Bill Amount Distribution')
plt.xlabel('Bills($)')
plt.ylabel('Count')
plt.show()



# box plot
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title('Bill Distribution by Day')
plt.xlabel('Days')
plt.ylabel('Total Bill($)')
plt.show()



# heat map
correlation_matrix = tips[['total_bill', 'tip', 'size']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()




# df = pd.DataFrame({
#     x: [1, 2, 3, 4, 5, 6],
#     y: [1, 2, 3, 4, 5, 6]
# })