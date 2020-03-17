# pandas er et dataanalyse module
from pandas import DataFrame
# matplotlib giver os mulighed for at plotte grafer 
import matplotlib.pyplot as plt
# sklearn indeholder kendte machine learning algoritmer og dataset
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris, load_wine

iris = load_iris()
features = iris.data.T
sepal_length = features[0]
sepal_width = features[1]
petal_length = features[2]
petal_width = features[3]

Data = {
	'x':sepal_length,
	'y':sepal_width
}

'''
wine = load_wine()
features = wine.data.T
Alcohol = features[0]
MalicAcid = features[1]


Data = {
	'x':Alcohol,
	'y':MalicAcid
}
'''

# laver 'Data' til en relevant datastruktur, så den kan bruges som argument i KMeans.fit()
df = DataFrame(Data,columns=['x','y'])
  
# sætter de første 'cluster'-centre (som senere bliver ændret)
kmeans = KMeans(n_clusters=1)

# komputerer k-means clustering ved at rykke rundt på centre og cluster-områder
kmeans.fit(df)

# notér central-punkterne ('centroids')
centroids = kmeans.cluster_centers_
print(centroids)

# vis graf
plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.xlabel("Sepal Length")
plt.ylabel("Speal Width")
plt.show()


	






