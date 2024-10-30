# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:19:52 2024

@author: Admin
"""

import pandas as pd
import numpy as np

df = pd.read_csv("D:\ML\Dataset\CandidateEliminationAlgCat.csv")

factors = np.array(df)[:, :-1]
target = np.array(df)[:, -1]

reverse=[]

for i in range(len(factors)-1,-1,-1):
    reverse.append(factors[i])

reverse=np.array(reverse)
print("Reversed Data Set: ")
print()
print(reverse)
print()


reverse_t=[]

for i in range(len(target)-1,-1,-1):
    reverse_t.append(target[i])

reverse_t=np.array(reverse_t)


general_hypothesis = [["?"] * len(reverse[0])] * len(reverse[0])

for i, val in enumerate(reverse_t):
    if val == "yes":
        specific_hypothesis = reverse[i].copy()
        break


for j, value in enumerate(reverse):
    if reverse_t[j] == "yes":
        for x in range(len(specific_hypothesis)):
            if value[x] != specific_hypothesis[x]:
                specific_hypothesis[x] = "?"
    else:
        for x in range(len(specific_hypothesis)):
           
            if specific_hypothesis[x] != "?":
                temp = ["?"] * len(specific_hypothesis)
                temp[x] = specific_hypothesis[x]
                if specific_hypothesis[x] != value[x]:
                    general_hypothesis[x] = temp
               
                

print("General Hypothesis: ")
for i in general_hypothesis:
    print(i)

print()
print("Specific Hypothesis: ")
print(specific_hypothesis)
