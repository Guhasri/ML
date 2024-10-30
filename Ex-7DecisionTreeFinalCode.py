import numpy as np
import pandas as pd
import math


def calculate_entropy(outcome):
    positive = np.sum(outcome == 1)
    negative = np.sum(outcome == 0)
    n = len(outcome)
    
    if positive == 0 or negative == 0:
        return 0
    
    positive_ratio = positive / n
    negative_ratio = negative / n
    
    return -(positive_ratio * math.log2(positive_ratio)) - (negative_ratio * math.log2(negative_ratio))


def calculate_information_gain(df, feature_column, outcome_column):
    
    table_entropy = calculate_entropy(outcome_column)
    
    
    values = df[feature_column].unique()
    feature_entropy = 0
    
    for value in values:
        subset = df[df[feature_column] == value]
        subset_entropy = calculate_entropy(subset[outcome_column].to_numpy())
        feature_entropy += (len(subset) / len(df)) * subset_entropy
        
    
    return table_entropy - feature_entropy


def build_tree(df, depth=0, max_depth=5):
    outcome_column = df.columns[-1]
    features = df.columns[:-1]
    
    
    if depth >= max_depth or len(df[outcome_column].unique()) == 1:
        return df[outcome_column].mode()[0]  
    
    
    gains = []
    for feature in features:
        gain = calculate_information_gain(df, feature, outcome_column)
        gains.append((feature, gain))
    
    
    best_feature, best_gain = max(gains, key=lambda x: x[1])
    
    
    tree = {best_feature: {}}
    
    
    for value in df[best_feature].unique():
        subset = df[df[best_feature] == value].drop(columns=[best_feature])
        subtree = build_tree(subset, depth + 1, max_depth)
        tree[best_feature][value] = subtree
    
    return tree


df = pd.read_csv("D:/ML/Dataset/DecisionTree.csv")


decision_tree = build_tree(df)

print(decision_tree)

