# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:09:29 2024

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt


day = np.array([5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7])
temperature = np.array([32, 32, 31, 32, 31, 29, 20, 32, 32, 31, 31, 29, 30, 31, 32, 32, 33, 33, 34, 34, 34, 34, 35, 32, 35, 35, 29, 29, 32, 33, 33])


def locally_weighted_regression(x, X, Y, tau):
    m = X.shape[0]
    W = np.exp(-((X - x) ** 2) / (2 * tau ** 2)) 
    X_b = np.c_[np.ones((m, 1)), X]  
    W_diag = np.diag(W) 
    theta = np.linalg.inv(X_b.T.dot(W_diag).dot(X_b)).dot(X_b.T).dot(W_diag).dot(Y)
    return np.array([1, x]).dot(theta)


tau = 0.5
X = day.reshape(-1, 1)
Y = temperature

x_new = np.linspace(1, 7, 100) 
y_pred = np.array([locally_weighted_regression(xi, day, temperature, tau) for xi in x_new])


plt.scatter(day, temperature, color='blue', label='Original Data')
plt.plot(x_new, y_pred, color='red', label='LWR Fit')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Locally Weighted Regression - Day vs Temperature')
plt.legend()
plt.show()