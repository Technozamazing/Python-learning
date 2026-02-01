import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
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



# Saving and loading the trained model:
from joblib import dump, load
dump(lin_model, 'tips_pred_joblib')

# Saving model + scaler (VERY IMPORTANT 🚨)
# If you used StandardScaler, LabelEncoder, etc., save them too:
# from joblib import dump, load

# dump(model, 'model.joblib')
# dump(scaler, 'scaler.joblib')


# Later:
# model = load('model.joblib')
# scaler = load('scaler.joblib')

# X_new = scaler.transform(X_new)
# pred = model.predict(X_new)