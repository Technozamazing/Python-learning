from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# workflow: Data -> Split -> Transform -> Fit -> Predict


# Sample data:
X = np.array([
    [400], [600], [800], [1000], [1200],
    [1400], [1600], [1800], [2000], [2200],
    [2500], [2800], [3000]
])

y = np.array([
    120, 180, 240, 310, 380,
    450, 520, 600, 680, 760,
    850, 940, 1020
])

# Data spliting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.18, random_state=42)

# Data scaling
scaler =  StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)   # use transform, not fit_transform -- as it has already learned & now can be applied.

# Training Model:
price_pred = LinearRegression()
price_pred.fit(X_train, y_train)

# Model prediction:
y_pred = price_pred.predict(X_test)
print('Actual Prices: ', y_test)
print('Predicted Prices: ', y_pred)

# Model Evaluation:
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Visualization:
plt.figure()
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()])  # perfect prediction line

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()
# sns.lineplot(data=data, x=y_test, y=y_pred, markers='o')
# plt.title('Model Evaluation based on prediction and actual data')

print('MAE: ', mae)
print('MSE: ', mse)
print('RMSE: ', rmse)
