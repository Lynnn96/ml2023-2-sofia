#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

# Function to get a positive integer input from the user
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Function to get a real number input from the user
def get_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a real number.")

# Get the number of points (N) and the number of neighbors (k)
N = get_positive_integer("Enter the number of points (N): ")
k = get_positive_integer("Enter the number of neighbors (k): ")

# Initialize arrays for storing points
points = np.zeros((N, 2))

# Collect N (x, y) points
for i in range(N):
    x = get_real_number(f"Enter x value for point {i+1}: ")
    y = get_real_number(f"Enter y value for point {i+1}: ")
    points[i] = [x, y]

# Check if k <= N
if k <= N:
    # Separate the points into X and Y components
    X_train = points[:, 0].reshape(-1, 1)
    Y_train = points[:, 1]

    # Create and train the k-NN regressor
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, Y_train)

    # Get the prediction point X and predict Y
    X_pred = get_real_number("Enter the value of X for prediction: ")
    Y_pred = knn_regressor.predict([[X_pred]])

    # Calculate the coefficient of determination (R² score)
    Y_train_pred = knn_regressor.predict(X_train)
    r2 = r2_score(Y_train, Y_train_pred)

    print(f"The predicted value of Y at X = {X_pred} is {Y_pred[0]}")
    print(f"Coefficient of Determination (R² score): {r2}")
else:
    print("Error: k must be less than or equal to N.")


# In[ ]:




