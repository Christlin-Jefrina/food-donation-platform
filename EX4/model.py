import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Predict and evaluate accuracy
y_pred = model.predict(x_test)
accu = accuracy_score(y_test, y_pred)
print("Model Accuracy before permutation:", accu)

# Permutation Feature Importance
pre_impor = permutation_importance(model, x_test, y_test, n_repeats=30, random_state=42)

# Extract feature importances
feature_importance = pre_impor.importances_mean
feature_name = iris.feature_names

# Print feature importance
print("\nPermutation Feature Importances:")
for importance, name in zip(feature_importance, feature_name):
    print(f"{name}: {importance:.4f}")

# Visualize with a bar chart
plt.barh(feature_name, feature_importance)
plt.xlabel("Importance Score")
plt.title("Permutation Feature Importance")
plt.show()
