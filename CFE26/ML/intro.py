# This is a sample introduction program to understand about Linear Regression and
# Logistic Regression.

from sklearn.linear_model import LinearRegression, LogisticRegression
import numpy as np


# Sample Data:
x = np.array([[1], [2], [3], [4], [5]])
y_cont = np.array([2, 4, 6, 8, 10])  # continuous target
y_bin = np.array([0, 0, 1, 1, 1])  # binary target


# Linear Regression:
lin_reg = LinearRegression()
lin_reg.fit(x, y_cont)
pred = lin_reg.predict([[10]])
print(f'Linear Regression Prediction: {pred}')


# Logistic Regression:
log_reg = LogisticRegression()
log_reg.fit(x, y_bin)
inp = int(input('Enter the value within 1 - 5: '))
print(f'Logistic Regression Probability for {inp}: {log_reg.predict_proba([[inp]])}')
print(f'Logistic Regression Probability: {log_reg.predict([[inp]])}')




# Now the question aries here:
# Upto now we have seen about the features, target(label), prediction in our sample program above
# Here we have a simple feature of one value

# Suppose we have a data set having features age and income
# age: 10 - 80
# income: 10,000 - 1,000,000

# Now the problem arise here:
# If we directly fit this features data to the model -- our model predicts inaccurately
# cause: due to imbalance in the feature data:
# age range from 10 to 80  whereas  income range 10,000 to 1,000,000
# income(large data) dominates the learning process thus the predication gets affected.

# To overcome this issue
# We use scaling(fit_transform) - Learn scaling parameters + apply scaling

# What actually happens:
# 1. fit: Learns properties of data (for scaling it learns:- mean, standard deviation, min/max)
# 2. transform: Uses learned values to change data.

# Doing so ensures the training and testing data is balanced.
# so the prediction comes accurate.

# workflow: Data -> Split -> Scaling(fit_transform) -> Fit -> Predict




# House price predication:
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# sample data:
x = np.array([[100], [300], [600], [700], [1200]])  # House size in sq.ft
y = np.array([120, 250, 435, 600, 900])  # House pricing in thousand

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=34)

# Performing scaling in feature:
scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

# Training the model:
pricing_model = LinearRegression()
pricing_model.fit(X_train, y_train)

# Model predication:
predication = pricing_model.predict(X_test)
print(f'Price prediction: {predication}')

# Evaluating Model:
mae = mean_absolute_error(y_test, predication)
mse = mean_squared_error(y_test, predication)
rmse = np.sqrt(mse)
print(f'Mean Absolute Error(MAE): {mae}')
print(f'Mean Squared Error(MSE): {mse}')
print(f'Root Mean Squared Error(RMSE): {rmse}')


# Here Conclusion of above program:
# Above we have 2 main constains that have resulted in high error:
# 1. Our training data set is very small only 5 sample -- which is very less for learning the pattern for our model.
# 2. We have seperately scaled train and test data:
#    So,
#    Our data is trained in one scale and tested in another scale
#    which arise the problem

# Our avg error is 426.25 and target(price) range is 120-900
# Which is 50% error --> Clearly Poor model.

# Improved in house_price_pred.py