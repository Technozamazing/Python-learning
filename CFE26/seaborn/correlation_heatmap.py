import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Sample dataset
df = sns.load_dataset("iris")
# Compute correlation matrix
corr_matrix = df.corr(numeric_only=True)
# Plot annotated heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
   corr_matrix,
   annot=True, # Show correlation values
   fmt=".2f", # Format to 2 decimal places
   cmap="coolwarm", # Color palette
   vmin=-1, vmax=1, # Fix color scale for correlations
   square=True, # Square cells for better symmetry
   linewidths=.5 # Lines between cells
)
plt.title("Correlation Matrix with Annotations")
plt.show()