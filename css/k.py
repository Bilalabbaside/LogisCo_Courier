from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
iris = datasets.load_iris()
X = iris.data[:,:4]
plt.scatter(X[:,0],X[:,1], c=iris.target)
plt.xlabel("sepel length", fontsize = 18)
plt.ylabel("sepel width", fontsize = 18)
km = KMeans(n_clusters = 3)
km.fit(X)
km.predict([[7.9,3.8,6.4,2]])
new_labels = km.labels_

fig,axes = plt.subplots(1,2,figsize = (16,8))
axes[0].scatter(X[:,0], X[:,1], c = iris.target)
axes[1].scatter(X[:,0], X[:,1], c = new_labels)

axes[0].set_xlabel("Sepel length", fontsize = 18)
axes[0].set_ylabel("Sepel Width", fontsize = 18)
axes[1].set_xlabel("Sepel length", fontsize = 18)
axes[1].set_ylabel("Sepel Width", fontsize = 18)

axes[0].tick_params(direction = 'in', length =10, width =5, colors = 'black',labelsize = 20)
axes[1].tick_params(direction = 'in', length =10, width =5, colors = 'black',labelsize = 20)

axes[0].set_title("Actual", fontsize=18)
axes[1].set_title("Predicted", fontsize=18)
plt.show()