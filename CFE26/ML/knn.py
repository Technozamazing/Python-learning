# workflow: Data -> Split -> Transform -> Fit -> Predict
# Reference: https://www.geeksforgeeks.org/machine-learning/k-nearest-neighbours/

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=42)

# KNeighborsClassifier model instance
knn = KNeighborsClassifier(n_neighbors=3)

# Instance training on Training Data
knn.fit(X_train, y_train)

# Making Prediction on Testing Data
y_pred = knn.predict(X_test)
print(f'Prediction: {y_pred}')

# Evaluating the accuracy of the instance:
acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {acc}')


# K-Nearest Neighbors (KNN) is a supervised machine learning algorithm generally used for 
# classification but can also be used for regression tasks. It works by finding the "k" 
# closest data points (neighbors) to a given input and makes a predictions based on the 
# majority class (for classification) or the average value (for regression).