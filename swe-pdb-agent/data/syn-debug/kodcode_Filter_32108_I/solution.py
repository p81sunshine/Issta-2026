import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

def k_means_clustering(points, k):
    """
    Clusters the points into k clusters using the k-means clustering algorithm.

    Parameters:
    points (np.ndarray): 2D array of points to be clustered.
    k (int): Number of clusters.

    Returns:
    tuple: (cluster_centers, labels, inertia)
        - cluster_centers (np.ndarray): Coordinates of cluster centers.
        - labels (np.ndarray): Labels of each point indicating to which cluster it belongs.
        - inertia (float): Sum of squared distances of samples to their closest cluster center.
    """
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(points)
    return kmeans.cluster_centers_, kmeans.labels_, kmeans.inertia_


def find_optimal_clusters(points, max_k):
    """
    Determines the optimal number of clusters using the elbow method.

    Parameters:
    points (np.ndarray): 2D array of points to be clustered.
    max_k (int): Maximum number of clusters to consider.

    Returns:
    tuple: (k_values, inertias)
        - k_values (list): List of k values.
        - inertias (list): List of inertia values corresponding to each k.
    """
    inertias = []
    k_values = range(1, max_k + 1)

    for k in k_values:
        _, _, inertia = k_means_clustering(points, k)
        inertias.append(inertia)

    return inertias, k_values


def plot_clusters(points, k, labels, cluster_centers):
    """
    Visualizes the clusters with different colors for each cluster.

    Parameters:
    points (np.ndarray): 2D array of points to be visualized.
    k (int): Number of clusters.
    labels (np.ndarray): Labels of each point indicating to which cluster it belongs.
    cluster_centers (np.ndarray): Coordinates of cluster centers.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', marker='o')
    plt.scatter(cluster_centers[0], cluster_centers[1], c='red', marker='x')
    plt.title('K-Means Clustering')
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.show()