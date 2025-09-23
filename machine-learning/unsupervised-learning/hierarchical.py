import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

X = np.array([[1, 2], [2, 3], [3, 4], [8, 8], [9, 9], [10, 10]])

Z = linkage(X, method='ward') ## Ward tenta minimizar a variância dentro dos clusters

plt.figure(figsize=(8, 4))
dendrogram(Z)
plt.title("Dendogram")
plt.xlabel("Amostras")
plt.ylabel("Distância")
plt.show()

clusters = fcluster(Z, t=2, criterion='maxclust')
print("Clusters: ", clusters)