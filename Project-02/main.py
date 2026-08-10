# Data Classification using AI

from sklearn.datasets import load_iris
import pandas as pd

# loading dataset
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print(df.head())
print(df.info())
print(df['target'].value_counts())

from sklearn.model_selection import train_test_split

# Features and target separate
X = df.drop('target', axis=1)  
y = df['target']                

# 80% Training, 20% Testing split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Model create and train
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

from sklearn.metrics import confusion_matrix

# Detailed breakdown of predictions
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
