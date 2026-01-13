# Filtering:
# Keeping the row that match a condition.

import pandas as pd
df = pd.read_csv("C:/Users/LOQ/OneDrive/Desktop/data.csv")
# print(df)

Boys = df[df['Sex'] == 'Male']
print(Boys)
print('\n')

Girls = df[df['Sex'] == 'Female']
print(Girls)
print('\n')

Chitwan_std = df[df['District'] == 'Chitwan']
print(Chitwan_std)
print('\n')

Kaski_std = df[df['District'] == 'Kaski']
print(Kaski_std)
print('\n')

Top_std = df[0:11]
print(Top_std)
print('\n')

Gandaki_std = df[(df['District'] == 'Chitwan') & (df['District'] == 'Lamjung')]
print(Gandaki_std)
print('\n')