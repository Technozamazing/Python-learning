# After training and evaluating our model we can save it to a file
# and recall it later to use it

# In Scikit learn we have two tools for that:
# 1. joblib - recommended
# 2. pickle - (works, but slower for large models)

# From our previous tips_pred model:

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error
# workflow: Data -> Split -> Transform -> Fit -> Predict


tips = sns.load_dataset('tips')
print(tips.info())

# Data Cleaning:
tips = tips.drop(['sex', 'smoker', 'day', 'time'], axis=1)
print(tips.columns)

# Data classification(feature, label(target)):
X = tips[['total_bill', 'size']]
y = tips.drop(['total_bill', 'size'], axis=1)

# Data splitting:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model:
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

# Model prediction:
# y_pred = lin_model.predict(X_test)
# print(f'Actual tips: {y_test}')
# print('Predicted tips: ', X_test,':', y_pred)

# Model Evaluation:
# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# rmse = root_mean_squared_error(y_test, y_pred)
# print('MAE: ', mae)
# print('MSE: ', mse)
# print('RMSE: ', rmse)


# Application:
t_bill = float(input("Enter the total bill paid: "))
size = int(input('Enter the size of the group (1 for single person): '))
user_input = pd.DataFrame(
    [[t_bill, size]],
    columns=['total_bill', 'size']
)
# input = np.array([[t_bill, size]])
prediction = lin_model.predict(user_input)
print("Predicted tip:", prediction[0][0])
# 7.56, 2 = 1.7852338083921855



import pickle

with open('tips_pred', 'wb') as f:
    pickle.dump(lin_model, f)

