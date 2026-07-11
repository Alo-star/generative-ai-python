import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Sample dataset
data = pd.DataFrame({
    'Experience': [1,2,3,4,5,6,7,8,9,10],
    'Salary': [30,35,40,45,50,55,60,65,70,75]
})

X = data[['Experience']]
y = data['Salary']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Results
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
print("R2 Score:", r2_score(y_test, y_pred))


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt


# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model parameters
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Visualization
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.xlabel("Years of Experience")
plt.ylabel("Salary (in thousands)")
plt.title("Linear Regression: Experience vs Salary")
plt.legend()
plt.show()