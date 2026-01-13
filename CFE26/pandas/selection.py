import pandas as pd
df = pd.read_csv("C:/Users/LOQ/OneDrive/Desktop/data.csv", index_col='Name')         # index_col  --> will make the column as the index
# print(df)


# Selection by Columns:
print(df['IOE Roll'])
print('\n')
print(df[['IOE Roll', 'District', 'Sex']])


# Selection by Rows:
print(df.loc['Anurag Adhikari'])
print('\n')
print(df.loc['Anurag Adhikari':'Bigyan Aryal', ['IOE Roll', 'Phone']])    # By slicing
print('\n')
print(df.loc[['Anurag Adhikari'], ['IOE Roll', 'Phone']])




# Searching...
while True:
    name = input("Enter the name of the student: ")
    try:
        print(df.loc[name])
        print('\n')
        break
    except KeyError:
        print(f'{name} not found in the database!')
        print('\n')
