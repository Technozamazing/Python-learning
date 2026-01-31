import seaborn as sns
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

# Data scaling:
# Not necessary: As features doesn't differ a lot in magnitude. 
# total_bill   → numeric (≈ 3 – 50)
# tip          → numeric (≈ 1 – 10)(Target)
# size         → numeric (1 – 6)
# others → categorical.

# Training the model:
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

# Model prediction:
y_pred = lin_model.predict(X_test)
print(f'Actual tips: {y_test}')
print('Predicted tips: ', X_test,':', y_pred)

# Model Evaluation:
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
print('MAE: ', mae)
print('MSE: ', mse)
print('RMSE: ', rmse)

# Visualization:
plt.figure()
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()])  # perfect prediction line

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()