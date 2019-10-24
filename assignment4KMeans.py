
# coding: utf-8

# In[42]:


import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
dataset = pd.read_csv('/home/rl20/Desktop/Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values


# Import k-means from sklearn

from sklearn.cluster import KMeans


for i in range(1, 11):

    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)

    kmeans.fit(X)

    
# Fitting K-Means to the dataset

kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)

y_kmeans = kmeans.fit_predict(X)



# Visualising the clusters

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 50, c = 'red', label = 'Cluster 1')

plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 50, c = 'blue', label = 'Cluster 2')

plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 50, c = 'green', label = 'Cluster 3')

plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 50, c = 'cyan', label = 'Cluster 4')

plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 50, c = 'magenta', label = 'Cluster 5')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 150, c = 'yellow', label = 'Centroids')

plt.title('Clusters of CUSTOMERS')

plt.xlabel('Annual Income (k$)')

plt.ylabel('Spending Score (1-100)')


plt.legend()

plt.show()

