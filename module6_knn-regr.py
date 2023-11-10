#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = []
        for x in X:
            # Calculate Euclidean distances between x and all training points
            distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
            # Find the indices of the k-nearest neighbors
            k_indices = np.argsort(distances)[:self.k]
            # Predict the output as the mean of the k-nearest neighbors' y values
            y_pred.append(np.mean(self.y_train[k_indices]))
        return np.array(y_pred)

# Input N (number of data points) and k (number of neighbors)
N = int(input("Enter the number of data points (N): "))
k = int(input("Enter the value of k: "))

# Check if k is valid
if k <= N:
    # Input the data points (x, y)
    data = []
    for i in range(N):
        x = float(input(f"Enter x-coordinate for data point {i + 1}: "))
        y = float(input(f"Enter y-coordinate for data point {i + 1}: "))
        data.append([x, y])

    # Convert data to a NumPy array
    data = np.array(data)

    # Input the value of X for prediction
    X = float(input("Enter the value of X for prediction: "))

    # Split the data into X and y
    X_data = data[:, 0].reshape(-1, 1)
    y_data = data[:, 1]

    # Create a k-NN Regression model
    knn = KNNRegression(k)
    knn.fit(X_data, y_data)

    # Predict the result for X
    result = knn.predict(np.array([[X]]))
    print(f"The result (Y) of k-NN Regression is: {result[0]}")
else:
    print("Error: k should be less than or equal to N.")


# In[ ]:




