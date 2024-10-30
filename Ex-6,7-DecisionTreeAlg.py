# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:30:36 2024

@author: Admin
"""

import numpy as np
import pandas as pd 
import math

df=pd.read_csv("D:/ML/Dataset/DecisionTree.csv")
outcome=np.array(df)[:,-1]
positive=0
negative=0
n=len(outcome)
for i in outcome:
    if i==0:
        negative+=1
    else:
        positive+=1

positive_ratio=positive/n
negative_ratio=negative/n
table_entropy=-(positive_ratio*math.log2(positive_ratio))-(negative_ratio*math.log2(negative_ratio))
print("Table Entropy: ",table_entropy)

looks_handsome=np.array(df)[:,:1]

S1=0
S2=0

positive=0
negative=0
positive1=0
negative1=0
n=0
n1=0

for i in range(len(looks_handsome)):
    if looks_handsome[i]==0:
        n+=1
        if outcome[i]==0:
            negative+=1
        else:
            positive+=1
    else:
        n1+=1
        if outcome[i]==0:
            negative1+=1
        else:
            positive1+=1

positive_ratio=positive/n
negative_ratio=negative/n
S1=-(positive_ratio*math.log2(positive_ratio))-(negative_ratio*math.log2(negative_ratio))
print("S1 Entropy(Looks_handsome): ",S1)

positive1_ratio=positive1/n1
negative1_ratio=negative1/n1
S2=-(positive1_ratio*math.log2(positive1_ratio))-(negative1_ratio*math.log2(negative1_ratio))
print("S2 Entropy(Looks_handsome): ",S2)
            
info_gain=table_entropy-(((n/7)*S1)+((n1/7)*S2))
    
print("Informtion gain(Looks handsome): ",info_gain)
    
    

    