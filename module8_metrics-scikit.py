#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from sklearn.metrics import precision_score, recall_score

def get_user_input():
    N = int(input("Enter the number of points (N): "))

    # Initialize arrays for X and Y
    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    # Get user inputs for N points
    for i in range(N):
        X[i] = int(input(f"Enter x value for point {i+1} (0 or 1): "))
        Y[i] = int(input(f"Enter y value for point {i+1} (0 or 1): "))

    return X, Y

def compute_metrics(X, Y):
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)
    return precision, recall

# Main program
X, Y = get_user_input()
precision, recall = compute_metrics(X, Y)

print(f"Precision: {precision}")
print(f"Recall: {recall}")

