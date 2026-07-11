import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#Generate sample data
x,y = make_blobs(n_samples=300,centers=3,random_state=42)

#apply K-means
Kmeans = KMeans(n_clusters=3,random_state=42)
Kmeans.fit(x)

#get cluster lables and centriodes
label=Kmeans.labels_
centroids= Kmeans.cluster_centers_

#plot the clusters
plt.scatter(x[:,0],x[:,1],c=label,cmap='viridis',s=50)
plt.scatter(centroids[:,0],centroids[:,1],c='red',marker='X',s=200)
plt.title("K-Means Clustering Example")
plt.show()