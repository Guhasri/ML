# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df= pd.read_csv('Dataset/airbnb.csv')


df_noNULL=df.dropna()
print("No NULL values: \n\n",df_noNULL[['id','bathrooms']].head())

#Mean

mean = df['bathrooms'].fillna(df['bathrooms'].mean())
print("\n\nMean: \n\n",df['id'].head(),"\t",mean.head())


#median

median = df['bathrooms'].fillna(df['bathrooms'].median())
print("\n\nMedian: \n\n",median.head())

#mode

mode = df['bathrooms'].fillna(df['bathrooms'].mode())
print("\n\nMode: \n\n",mode.head())

#IQR

my_data= df['reviews']
sorted_data=np.sort(my_data)

Q1=np.percentile(sorted_data,25,method='midpoint')
Q2=np.percentile(sorted_data,50,method='midpoint')
Q3=np.percentile(sorted_data,75,method='midpoint')

IQR=Q3-Q1

lower_limit=Q1 -1.5*IQR
upper_limit=Q3 +1.5*IQR
print("Lower limit: ",lower_limit,"\nUpper limit: ",upper_limit)


plt.figure()
sns.boxplot(sorted_data)
plt.figure()
sns.histplot(my_data)
plt.figure(figsize=(22,6))
sns.barplot(x=df['reviews'],y=df['rating'])
plt.xticks(rotation=30, ha='right')



















