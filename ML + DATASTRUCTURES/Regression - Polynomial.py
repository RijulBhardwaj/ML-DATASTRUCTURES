import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Data points
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# Polynomial regression model (degree 3)
mymodel = np.poly1d(np.polyfit(x, y, 3))

# Calculate R² score
r2 = r2_score(y, mymodel(x))
print(f"R² Score: {r2}")

# Prediction for new data point
new_x = 17
speed = mymodel(new_x)
print(f"Predicted speed for x={new_x}: {speed}")

# Plot data points
plt.scatter(x, y, label='Data points')

# Plot polynomial regression line
x_line = np.linspace(min(x), max(x), 100)
y_line = mymodel(x_line)
plt.plot(x_line, y_line, color='red', label='Polynomial regression line (degree 3)')

# Plot new prediction point
plt.scatter(new_x, speed, color='green', s=100, label=f'Prediction for x={new_x}')


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression (degree 3)')
plt.legend()


plt.show()
