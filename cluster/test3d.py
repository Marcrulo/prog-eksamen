from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv, to_numeric
from sklearn.cluster import KMeans
import numpy as np


categories = ["date","driving","drugs","lethal","other","stealing","violence"]
df = read_csv("../../csv/crime.csv", sep=";", names=categories)
for item in categories[1:]:
	df[item] = df[item].str.replace('\'','').astype(int)

kmeans = KMeans(n_clusters=2).fit(df[["driving","drugs","other"]])
centroids = kmeans.cluster_centers_
print(centroids)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x =[1,2,3,4,5,6,7,8,9,10]
y =[5,6,2,3,13,4,1,2,4,8]
z =[2,3,3,3,5,7,9,11,9,10]



ax.scatter(df['driving'], df['drugs'], df['other'], c=kmeans.labels_.astype(float), marker='o',s=50, alpha=0.5)
ax.scatter(centroids[:, 0], centroids[:, 1],centroids[:,2], c='black', s=50)

ax.set_xlabel('driving')
ax.set_ylabel('drugs')
ax.set_zlabel('other')

plt.show()