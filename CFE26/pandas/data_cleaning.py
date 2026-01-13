# Data Cleaning:
# The process of fixing/removing:
# Incomplete, Incorrect, or Irrelevant data  -->   around 75% of work done with pandas is data cleaning.

import pandas as pd
df = pd.read_csv("C:/Users/LOQ/OneDrive/Desktop/students_marks_extended.csv")
print(df)
print('\n')



# 1. Drop irrelevent columns
df = df.drop(columns=['SN', 'Section', 'Total', 'Percentage'])
print(df)



# 2. Handle missing data
#    dropna = Drop Not Available
df = df.dropna(subset=['Physics', 'Mathematics', 'Chemistry'])    # Any Columns in this "subset list" will drop those rows if they are missing a value.
print(df)

#    fillna = Fill Not Available
df = df.fillna({'Physics': 'None', 'Chemistry': 'Absent', 'Mathematics': 'NQ'})
print(df)



# 3. Fix inconsistent values
df['Gender'] = df['Gender'].replace({'Male': 'MALE', 'Female': 'FEMALE'})
print(df)



# 4. Standardize text
df['Name'] = df['Name'].str.upper()
print(df)



# 5. Fix or change data types
df['Differently_able'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
df['Differently_able'] = df['Differently_able'].astype('bool')
print(df)



# 6. Remove Duplicate values
df = df.drop_duplicates()
print(df)