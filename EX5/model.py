# model.py
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# Load data and train model
iris = load_iris()
X, y = iris.data, iris.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the model
joblib.dump(model, 'iris_model.pkl')
