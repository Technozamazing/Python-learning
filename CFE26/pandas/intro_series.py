# Indexing:
# Series
# DataFrames
# Importing
# Selection
# Filtering
# Aggregation
# Data cleaning


# Pandas is a python library, build on top-off NumPy
# Pandas = Panal + Data
# Using this library -- we typically works with objects called  --->  "Series" -- One dimensional  &&  "Dataframe" -- Two dimensional

import pandas as pd
import numpy as np

# print(pd.__version__)
# print('\n')




# # Series:
# # A Pandas One dimensional "labeled array" that can hold any data type
# # Think of it like a single column in a spreadsheet (1-Dimensional)

# data = ["Roll Number", 'PAS080BEI025', 'PAS080BEI026', 'PAS080BEI027', 'PAS080BEI028', 'PAS080BEI029', 'PAS080BEI030']
# series = pd.Series(data, index=['Name', 'Rajeev Yadav', 'Roman Shrestha', 'Roshan Sapkota', 'Sagar Panth', 'Samana Pandit', 'Sanam Chunara'])    # Here "Series" is a Constructor -- not a function/method
# # Here Index can be any thing -- a list, tuple, dictionary, NumPy array or even a series
# print(series)
# print('\n')







# # Accessing a value directly from a series

# # loc --> locating a value by its label(index)
# # iloc --> locating a value by its integer index(position) [0, 1, 2, 3, 4, 5, ..]      -----> Similar to accessing an Array in other language 
# # Filter by Value --> Accessing a value by Using sub-script operator


# print(series.loc['Roman Shrestha'])
# print('\n')

# # Update(reassign) values we use Sub-script operator with loc:
# series.loc['Sanam Chunara'] = np.nan
# print(series)

# # Using iloc
# print(series.iloc[2])


# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_series = pd.Series(num, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])

# print(num_series[num_series >= 4])




# Working with dictionaries:

# Study Hours in a day:
# Assuming I have promissed to study 5 hours bare minimum
hours = { 'Day 1': 4, 'Day 2':5, 'Day 3':7, 'Day 4':1, 'Day 5':9, 'Day 6':16, 'Day 7':int(0.25)}           # Will not use default index or a seperate index, will use key as index.
std_hrs = pd.Series(hours, name='Studied Hours')
std_hrs.index.name = 'Days'
print(std_hrs)

std_hrs.loc['Day 7'] += 3
print(std_hrs)

print(std_hrs[std_hrs >= 5])