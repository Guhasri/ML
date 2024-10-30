import pandas as pd
import numpy as np

df = pd.read_csv("D:\\ML\\Dataset\\CandidateEliminationAlgCat.csv")

factors = np.array(df)[:, :-1]
target = np.array(df)[:, -1]

# Initialize the specific hypothesis with the first positive example or the most specific one
specific_hypothesis = ["?"] * len(factors[0])
general_hypothesis = [["?"] * len(factors[0])] * len(factors[0])

for i, val in enumerate(target):
    if val == "yes":
        specific_hypothesis = factors[i].copy()
        break

memo = []

for j, value in enumerate(factors):
    if target[j] == "yes":
        for x in range(len(specific_hypothesis)):
            if value[x] != specific_hypothesis[x]:
                specific_hypothesis[x] = "?"
    else:
        for x in range(len(specific_hypothesis)):
            temp = ["?"] * len(specific_hypothesis)
            temp[x] = specific_hypothesis[x]
            if specific_hypothesis[x] != "?" and x not in memo:
                if specific_hypothesis[x] != value[x]:
                    general_hypothesis[x] = temp
                else:
                    general_hypothesis[x] = ["?"] * len(specific_hypothesis)
                    memo.append(x)
            else:
                general_hypothesis[x] = ["?"] * len(specific_hypothesis)
                memo.append(x)

print("General Hypothesis: ")
for i in general_hypothesis:
    if i != ["?"] * len(factors[0]):
        print(i)

print()
print("Specific Hypothesis: ")
print(specific_hypothesis)
