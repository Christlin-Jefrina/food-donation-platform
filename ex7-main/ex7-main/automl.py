import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_iris
from tpot import TPOTClassifier
import joblib
import os

# Load dataset from sklearn
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# No need to manually encode y because sklearn's iris already has numeric labels

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# AutoML with TPOT
tpot = TPOTClassifier(generations=5, population_size=20, random_state=42)
tpot.fit(X_train, y_train)

# Evaluate
score = tpot.score(X_test, y_test)
print(f"Accuracy: {score}")

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Save the best model
tpot.export("models/best_model.py")
joblib.dump(tpot.fitted_pipeline_, "models/best_model.pkl")
