# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:49:52 2024

@author: Admin
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('D:/ML/Dataset/regression1.csv')

x=df['Monthly Sales'].values.reshape(-1,1)
y=df['Online Advertising'].values.reshape(-1,1)

regressor=LinearRegression()
regressor.fit(x,y)

x_pred=regressor.predict(x)

print("Predicted Values: ",x_pred)
plt.scatter(x,y,color="blue")
plt.plot(x,x_pred,color="red")
plt.xlabel("Monthly Sales")
plt.ylabel("Online Advertising")
plt.show()


#negative correlation
print()
print()

df = pd.read_csv('D:/ML/Dataset/regression2.csv')

x=df['CarAge'].values.reshape(-1,1)
y=df['Price'].values.reshape(-1,1)

regressor=LinearRegression()
regressor.fit(x,y)

x_pred=regressor.predict(x)

print("Predicted Values: ",x_pred)
plt.scatter(x,y,color="blue")
plt.plot(x,x_pred,color="red")
plt.xlabel("Monthly Sales")
plt.ylabel("Online Advertising")
plt.show()







