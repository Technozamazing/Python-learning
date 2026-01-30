import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print(sns.__version__)


# Seaborn comes with several builtin datasets
tips = sns.load_dataset('tips')
print(tips.head(-1))
print('\n')
print(tips.shape)
print('\n')
print(tips.info())
