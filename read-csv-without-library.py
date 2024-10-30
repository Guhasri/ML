# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:16:05 2024

@author: Admin
"""

        
def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    #headers = lines[0].strip().split(',')
    rows = []
    for line in lines:
        columns = line.strip().split(',')
        row = [columns[i] for i in range(6)]
        rows.append(row)
    return rows
    
file_path="D:\ML\Dataset\CandidateEliminationAlg.csv"
df=read_csv(file_path)
print(df[1][1:])