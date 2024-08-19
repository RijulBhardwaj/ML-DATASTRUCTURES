import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# seed determines how many random variables are set so training and testing dataset remains uniform
np.random.seed(42)

# Generating a large dataset
n_samples = 1000000
X = np.random.rand(n_samples, 1) * 100  # Feature
noise = np.random.randn(n_samples, 1) * 10  # Noise
y = 5 * X + 20 + noise  # Target with a linear relationship

# Create a DataFrame
data = pd.DataFrame(np.hstack([X, y]), columns=['Feature', 'Target'])
print(data.head())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[['Feature']], data['Target'], test_size=0.2, random_state=42)

# Create the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Function to predict and evaluate on new data
def predict_and_evaluate(model, X_new):
    y_new_pred = model.predict(X_new)
    return y_new_pred

# Generate new arti data for predictions
X_new = np.array([[10], [50], [90]])
y_new_pred = predict_and_evaluate(model, X_new)

# Display the new predictions
for feature, pred in zip(X_new, y_new_pred):
    print(f"Feature: {feature[0]}, Predicted Target: {pred:.2f}")

# Function to display model coefficients
def display_model_coefficients(model):
    print("Model Coefficients:")
    print(f"Intercept: {model.intercept_}")
    print(f"Coefficient: {model.coef_[0]}")

# Display the model coefficients
display_model_coefficients(model)


#adding matpotlib

# Plotting the data
plt.figure(figsize=(12, 6))

# Plot training data
plt.subplot(1, 2, 1)
plt.scatter(X_train, y_train, alpha=0.3, label='Training data')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Training Data')

# Plot test data and predictions
plt.subplot(1, 2, 2)
plt.scatter(X_test, y_test, alpha=0.3, color='green', label='Test data')
plt.scatter(X_test, y_pred, alpha=0.3, color='red', label='Predictions')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Test Data and Predictions')
plt.legend()

# Plot the regression line and new predictions
plt.figure(figsize=(12, 6))
plt.scatter(X, y, alpha=0.1, label='Data')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.scatter(X_new, y_new_pred, color='blue', s=100, label='New Predictions')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Regression Line and Predictions on New Data')
plt.legend()

plt.tight_layout()
plt.show()