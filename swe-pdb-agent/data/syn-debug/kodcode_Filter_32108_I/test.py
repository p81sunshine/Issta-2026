from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
from solution import k_means_clustering, find_optimal_clusters, plot_clusters

def test_k_means_clustering_basic():
    points = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    cluster_centers, labels, inertia = k_means_clustering(points, 2)
    assert len(cluster_centers) == 2
    assert len(labels) == len(points)
    assert inertia >= 0

def test_find_optimal_clusters_basic():
    points = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    k_values, inertias = find_optimal_clusters(points, 5)
    assert len(k_values) == 5
    assert len(inertias) == 5
    assert all(isinstance(value, int) for value in k_values)
    assert all(inertia >= 0 for inertia in inertias)

def test_plot_clusters():
    points = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    cluster_centers, labels, _ = k_means_clustering(points, 2)
    # For visual functions, we do not have assert here, just ensure it runs without error
    plot_clusters(points, 2, labels, cluster_centers)

def test_k_means_clustering_different_k():
    points = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
    for k in range(1, 4):
        cluster_centers, labels, inertia = k_means_clustering(points, k)
        assert len(cluster_centers) == k
        assert len(labels) == len(points)
        assert inertia >= 0