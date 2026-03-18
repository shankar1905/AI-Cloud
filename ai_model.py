from sklearn.linear_model import LinearRegression
import numpy as np

# Data
x = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Model
model = LinearRegression()
model.fit(x, y)

# Prediction
result = model.predict([[5]])

print("Prediction:", result)