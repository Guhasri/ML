# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:08:52 2024

@author: Admin
"""
with open("D:\ML\Dataset\CandidateEliminationAlgCat.csv", 'r') as file:
    lines = file.readlines()
    rows = []
    target=[]
    for line in lines:
        columns = line.strip().split(',')
        row = [columns[i] for i in range(6)]
        rows.append(row)
        target.append(columns[6])

target=target[1:]
rows=rows[1:]

reverse=[]

for i in range(len(rows)-1,-1,-1):
    reverse.append(rows[i])


print("Reversed Data Set: ")
print()
print(reverse)
print()

reverse_t=[]

for i in range(len(target)-1,-1,-1):
    reverse_t.append(target[i])

print(reverse_t)
print()

general_hypothesis = [["?"] * len(reverse[0])] * len(reverse[0])

no_of_generalization=0
order={}
final_order=[1,-1,-1,-1]
abc=[1]

for i, val in enumerate(reverse_t):
    if val == "yes":
        specific_hypothesis = reverse[i].copy()
        break

for j, value in enumerate(reverse):
    if reverse_t[j] == "yes":
        for x in range(len(specific_hypothesis)):
            if value[x] != specific_hypothesis[x]:
                no_of_generalization+=1
                specific_hypothesis[x] = "?"
        order[j+1]=no_of_generalization
        no_of_generalization=0
    else:
        final_order[j]=-2
        abc.append(j)
        for x in range(len(specific_hypothesis)):
           
            if specific_hypothesis[x] != "?":
                temp = ["?"] * len(specific_hypothesis)
                temp[x] = specific_hypothesis[x]
                if specific_hypothesis[x] != value[x]:
                    general_hypothesis[x] = temp
order.pop(1)               

    

while len(order.keys()) !=0:
    c=max(order.keys())
    final_order[max(abc)+1]=c
    abc.append(max(abc)+1)I
    order.pop(c)
    
    
print("Final order:", final_order)
 




print("General Hypothesis: ")
for i in general_hypothesis:
    print(i)

print()
print("Specific Hypothesis: ")
print(specific_hypothesis)
