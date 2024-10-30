# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:17:38 2024

@author: Admin
"""

def weightForz(z,w,lr):
    for i in z:
        cOut=0
        for j in range(0,2):
            cOut+=w[j]*i[j]
        if cOut >= 1:
            cOut=1
        else:
            cOut=0
        if cOut==i[2]:
            continue
        else:
            for k in range(0,2):
                w[k]+=lr*(i[2]-cOut)*i[k]
            j=0
    print(w)
    
z1=[[0,0,0],[0,1,0],[1,0,1],[1,1,0]]
z2=[[0,0,0],[0,1,1],[1,0,0],[1,1,0]]
data=[[0,0,0],[0,1,1],[1,0,1],[0,0,0]]

w1j=[1,1]
w2j=[1,1]
xorw=[1,1]

lr=1.5

weightForz(z1, w1j, lr)
weightForz(z2, w2j, lr)
weightForz(data, xorw , lr)


