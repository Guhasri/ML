# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:12:03 2024

@author: Admin
"""

def iteration(data):
    w=[0,0]
    b=0
    dw=[0,0]
    db=0
    lr=1
    
    for i in data:
        t=i[2]
        summation=b
        for j in range(0,2):
            summation+=i[j]*w[j]
        cOut=2
        if(summation<0):
            cOut=-1
        elif (summation>0):
            cOut=1
        else:
            cOut=0
        if(cOut==t):            
            continue
        else:
            for k in range(0,2):
                dw[k]=lr*t*i[k]
                w[k]+=dw[k]
            db=lr*t
            b+=db
    print("Final Weight: ",w,"Final bias: ",b)
    
    

import pandas as pd
import numpy as np

df=pd.read_csv("D:/ML/Dataset/ANN.csv", header=None)
data=np.array(df)
count=1

iteration(data)

    