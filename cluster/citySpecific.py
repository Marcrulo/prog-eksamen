from pandas import DataFrame, read_csv, to_numeric
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

months = ['januar', 'februar', 'marts','april','maj','juni','juli','august','september','oktober','november','december']
categories = ["date","driving","drugs","lethal","other","stealing","violence","severity","city"]

monthAverage = 100000000000#30.4368499
cityName = 'helsinge'

df = read_csv("../csv/crime.csv", sep=";", names=categories)
for item in categories[1:-1]:
	df[item] = df[item].str.replace('\'','').astype(int)

for i in range(len(df['date'])):
	for month in months:
		if month in str(df['date'][i]):
			df.loc[i,'date']= monthAverage*(months.index(month)+1)

#print(df['date'])

#df = df[df['city']=='hillerød']
df = DataFrame(df.loc[df['city'].str.contains(cityName,case=False)])
print(df)

kmeans = KMeans(n_clusters=12).fit(df[["date","severity"]])
centroids = kmeans.cluster_centers_

averageList = []
for item in centroids:
	averageList.append(item[1])
average = sum(averageList)/12

print(average)


ticks = []
for i in range(1,13):
	ticks.append(monthAverage*i)
labels = ['Jan', 'Feb', 'Mar', 'Apr','Maj','Jun','Jul','Aug','Sep','Okt','Nov','Dec']

plt.figure()
plt.axhline(average,0,10000000,color='purple')
plt.xticks(ticks, labels,rotation=20)
#plt.show()

plt.title(label=cityName.capitalize())
plt.scatter(df['date'], df['severity'], s=50, alpha=0.5, c= kmeans.labels_.astype(float))
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.xlabel("Date")
plt.ylabel("Severity")
plt.show()