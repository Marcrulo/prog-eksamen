from pandas import DataFrame, read_csv, to_numeric
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

'''
Data = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
       }

inp = read_csv("../../csv/crime.csv", sep=';', header=None)
Data = {
	 'x':inp.iloc[:,1],
	 'y':inp.iloc[:,2]
	 }


df = DataFrame(Data,columns=['xx','yy'])
'''
#df['xx'] = df['xx'].astype(int)
#df['yy'] = df['yy'].astype(int)
#print(df.dtypes)
#print(df['xx'])

df = read_csv("../../csv/crime.csv", sep=";", names=["date","driving","drugs","lethal","other","stealing","violence"])
#df = read_csv("../../csv/test.csv", sep=";", names=["driving","drugs"])
df["driving"] = df["driving"].str.replace('\'','').astype(int)
df["drugs"] = df["drugs"].str.replace('\'','').astype(int)
df["lethal"] = df["lethal"].str.replace('\'','').astype(int)
df["other"] = df["other"].str.replace('\'','').astype(int)
df["stealing"] = df["stealing"].str.replace('\'','').astype(int)
df["violence"] = df["violence"].str.replace('\'','').astype(int)

kmeans = KMeans(n_clusters=2).fit(df[["driving","drugs"]])
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['driving'], df['drugs'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()