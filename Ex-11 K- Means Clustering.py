# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:09:34 2024

@author: Admin
"""

import numpy as np


points = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])


centers = np.array([[2, 10], [5, 8], [1, 2]])


def manhattan_distance(p1, p2):
    return np.sum(np.abs(p1 - p2))


def assign_clusters(points, centers):
    clusters = []
    for point in points:
        distances = [manhattan_distance(point, center) for center in centers]
        cluster = np.argmin(distances)
        clusters.append(cluster)
    return clusters


def recalculate_centroids(points, clusters, k):
    new_centers = []
    for i in range(k):
        cluster_points = points[np.array(clusters) == i]
        if len(cluster_points) > 0:
            new_center = np.mean(cluster_points, axis=0)
        else:
            new_center = np.array([0, 0])
        new_centers.append(new_center)
    return np.array(new_centers)


k = 3
iterations = 2
for iteration in range(iterations):
    clusters = assign_clusters(points, centers)
    centers = recalculate_centroids(points, clusters, k)
    print(f"Iteration {iteration + 1} cluster centers:\n{centers}")


final_clusters = assign_clusters(points, centers)
print(f"Final cluster assignments: {final_clusters}")
