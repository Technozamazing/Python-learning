# We can import CSV(Comma Seperated Values) or JSON(JavaScript Object Notation) files with pandas to work with datas.


import pandas as pd
df = pd.read_csv("C:/Users/LOQ/OneDrive/Desktop/data.csv")
print(df)
print('\n')

new_json = pd.read_json("C:/Users/LOQ/Downloads/sample1.json")
print(new_json.to_string())       # to_string()  --->  if a table or data is shown truncated, it helps in viewing fully.

