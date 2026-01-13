# Dataframes:
# A tabular data structure with ROWS and COLUMNS. (2 Dimensional)
# Similar to an Excel Spreadsheet

import pandas as pd
import numpy as np

# # Converting a series into a DataFrame:
# num = [25, 26, 27, 28, 29, 30]
# num_series = pd.Series(num, index=['Rajeev Yadhav', 'Roman Shrestha', 'Roshan Sapkota', 'Sagar Panth', 'Samana Pandit', 'Sanam Chunara'])
# num_series.index.name = 'Student Names'

# # Convert the Series to a DataFrame and set the column name
# df = num_series.to_frame(name = 'Student Roll')
# # df = df.reset_index()  --> will reset the index to default [0, 1, 2, ..]   and convert any existing custom index to a seperate column.
# print(df)



employee = {
    'Name': ['Ramesh Poudel', 'Gita Sunar', 'Shakshyam Pradhan', 'Gokul Bastola'],
    'Age': [34, 44, 31, 28],
    'Salary': [43000, 45000, 56000, 23000],
    'Differently_able': [False, False, False, True]
}

df = pd.DataFrame(employee, index = list(range(1, 5)))
print(df)
print('\n')
print(df.loc[3])
print('\n')
print(df.loc[4])
print('\n')


# Adding a new column:
df['Gender'] = ['Male', 'Female', 'Male', 'Male']
print(df)
print('\n')


# Adding a new row:        --> create a new dataframe then concatinate.
new_row = pd.DataFrame([{'Name': 'Raman Budathoki', 'Age': 56, 'Salary': 45000, 'Differently_able': True, 'Gender': 'Male', 'PAN': int(3423567)},
                        {'Name': 'Srijana Manandhar', 'Age': 45, 'Salary': 55000, 'Differently_able': False, 'Gender': 'Female', 'PAN': int(7813567)},
                        {'Name': 'Smirti Shrestha', 'Age': 28, 'Salary': 30000, 'Gender': 'Female', 'PAN': int(7813000)}], index=[5, 6, 7])
df['PAN'] = [3423509, 3494667, 4563567, 3426120]     # There wasn't a PAN column in "df", so we added to remove "NaN" value.
updated = pd.concat([df, new_row])
print(updated)