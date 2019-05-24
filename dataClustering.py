# Libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

dataset = pd.read_csv("data/final-data.csv")

X = dataset[['Bus_Company', 'Bus_Delay']].values

# ---------------------------------------------------- K-Means ---------------------------------------------------------
# Calculate (by Elbow Method) the best count of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("The Elbow Method")
plt.xlabel('Number of clusters')
plt.ylabel("WCSS")
plt.show()

# Fitting by K-Means method to the dataset
centroidsCount = 3
kmeans = KMeans(n_clusters=centroidsCount, init='k-means++', random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Visualisation of the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=30, c='red', label='Cluster1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=30, c='blue', label='Cluster2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=30, c='green', label='Cluster3')
# plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=30, c='cyan', label='Cluster4')
# plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=30, c='magenta', label='Cluster5')

# Plot centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='yellow', label="centroids")

plt.title("Bus Delays clustering")
plt.xlabel(X[0])
plt.ylabel(X[1])
plt.legend()
plt.show()

# ----------------------------------------------- Affinity Propagation -------------------------------------------------
# TODO: affinity propagation

print("END")