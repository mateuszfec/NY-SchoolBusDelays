# Libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
from itertools import cycle
import time

startTime = time.time()

dataset = pd.read_csv("data/data10.csv")

X = dataset[['Boro', 'Bus_Delay']].values

algorithmKMeans = True
algorithmAffProp = False
algorithmMeanShift = True

# ---------------------------------------------------- K-Means ---------------------------------------------------------
if algorithmKMeans:
    startTimeKMeans = time.time()

    # Calculate (by Elbow Method) the best count of clusters
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    # plt.plot(range(1, 11), wcss)
    # plt.title("The Elbow Method")
    # plt.xlabel('Number of clusters')
    # plt.ylabel("WCSS")
    # plt.show()

    # Fitting by K-Means method to the dataset
    centroidsCount = 3
    kmeans = KMeans(n_clusters=centroidsCount, init='k-means++', random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    # Visualisation of the clusters
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=30, c='red', label='Cluster1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=30, c='blue', label='Cluster2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=30, c='green', label='Cluster3')

    # Plot centroids
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='yellow', label="centroids")

    plt.title("Bus Delays clustering")
    plt.xlabel(X[0])
    plt.ylabel(X[1])
    plt.legend()
    plt.show()
    endTimeKMeans = time.time()

# ----------------------------------------------- Affinity Propagation -------------------------------------------------
if algorithmAffProp:
    startTimeAffinity = time.time()

    # Compute Affinity Propagation
    af = AffinityPropagation(preference=-150).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_

    # Calculate number of clusters
    n_clusters_ = len(cluster_centers_indices)
    #print('Estimated number of clusters: %d' % n_clusters_)

    # Plot results
    plt.close('all')
    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        class_members = labels == k
        cluster_center = X[cluster_centers_indices[k]]
        plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=10)
        for x in X[class_members]:
            plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.xlabel(X[0])
    plt.ylabel(X[1])
    plt.show()
    endTimeAffinity = time.time()

# --------------------------------------------------- Mean-Shift -------------------------------------------------------
if algorithmMeanShift:
    startTimeMeanShift = time.time()

    # Compute clustering with MeanShift
    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    # Calculate number of clusters
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    #print("number of estimated clusters : %d" % n_clusters_)

    # Plot result
    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()
    endTimeMeanShift = time.time()

# Script time measurement
endTime = time.time()

if algorithmKMeans:
    print('K-Means exec time: ', round(endTimeKMeans - startTimeKMeans, 2), 's')
if algorithmAffProp:
    print('Affinity Propagation exec time: ', round(endTimeAffinity - startTimeAffinity, 2), 's')
if algorithmMeanShift:
    print('Mean-Shift exec time: ', round(endTimeMeanShift - startTimeMeanShift, 2), 's')

print('Summary exec time: ', round(endTime - startTime, 2), 's')
