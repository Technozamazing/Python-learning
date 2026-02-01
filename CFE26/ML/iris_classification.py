import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# workflow: Data -> Split -> Transform -> Fit -> Predict

iris = sns.load_dataset('iris')
# print(iris)

count = iris['species'].value_counts()
print(count)

# Data cleaning:
# 1. We do not have any null values or incorrect values
# 2. No need to drop colums as every colums is need to define the Target

# Data Classification(fetaures|label(Target)):
X = iris.drop(['species'], axis=1)
y = iris['species']

# As our prediction will be multi-class classification
# We will be encoding 'setosa', 'versicolor', 'virginica' to respective 0, 1, 2.
le = LabelEncoder()
le.fit(y)    # learn
y_encoded = le.transform(y)    # Apply
print(le.classes_)


# Data splitting:
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Data scaling(transform):
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model Training:
log_model = LogisticRegression()
log_model.fit(X_train, y_train)

# Model Prediction:
y_pred = log_model.predict(X_test)
print(f'Actual value: {y_test}')
print(f'Predicted value: {y_pred}')

# Model Evaluation:
acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {acc}')

# Visualization:
sns.pairplot(iris, hue="species", diag_kind="kde")
plt.suptitle("Iris Feature Relationships", y=1.02)
plt.show()