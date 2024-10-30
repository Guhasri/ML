# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:09:54 2024

@author: Admin
"""

from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import numpy as np


data = np.array([18, 22, 25, 42, 27, 43]).reshape(-1, 1)


Z = linkage(data, method='single', metric='euclidean')


plt.figure(figsize=(8, 5))
dendrogram(Z, labels=data.flatten(), distance_sort='ascending')
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()
