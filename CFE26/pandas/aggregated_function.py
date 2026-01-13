# Aggregated Function:
# Reduce a set of values into a single summary value.
# Used to summarize and analyze data often used with the groupby() function.

import pandas as pd
df = pd.read_csv("C:/Users/LOQ/OneDrive/Desktop/students_marks_extended.csv")
# print(df)


# Whole Dataframe:    Performs operation on whole dataframe
print(df.count())
print('\n')
print(df.mean(numeric_only = True))
print('\n')
print(df.median(numeric_only = True))
print('\n')
print(df.sum(numeric_only = True))
print('\n')
print(df.max(numeric_only = True))
print('\n')
print(df.min(numeric_only = True))
print('\n')





# Single Column:      Performs operation only on specified column
print(df['Mathematics'].max())   # No need to specify numeric_only cause --> math is a numric column
print('\n')
print(df['Mathematics'].min())
print('\n')
print(df['Chemistry'].max())
print('\n')
print(df['Chemistry'].min())
print('\n')
print(df['Physics'].sum())
print('\n')





# GroupBy()  --> This function(groupby) is used to split data into groups, apply an operation, and combine the results.
sex = df.groupby('Gender')
print(sex.sum(numeric_only=True))
print('\n')
print(sex.min(numeric_only=True))
print('\n')
print(sex.max(numeric_only=True))

section = df.groupby('Section')
print(section.sum(numeric_only=True))
print('\n')
print(section.min(numeric_only=True))
print('\n')
print(section.max(numeric_only=True))