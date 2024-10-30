# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 10:02:51 2024

@author: Admin
"""

import pandas as pd
import numpy as np

df=pd.read_csv("D:\ML\Dataset\FindSAlg.csv")

factors=np.array(df)[:,:-1]

target=np.array(df)[:,-1]

for i,val in enumerate(target):
    if val=="Yes":
        specific_hypothesis=factors[i].copy()
        break
for j,value in enumerate(factors):
    if target[j]=="Yes":
        for x in range(len(specific_hypothesis)):
            if value[x] != specific_hypothesis[x]:
                specific_hypothesis[x]="?"
print(specific_hypothesis)
            
    
