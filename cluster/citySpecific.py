from pandas import DataFrame, read_csv, to_numeric
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

months = ['januar', 'februar', 'marts','april','maj','juni','juli','august','september','oktober','november','december']
categories = ["date","driving","drugs","lethal","other","stealing","violence","severity","city"]

monthAverage = 100000000000#30.4368499
#DET HER ER NYT
cityNames = ['Ballerup','Smørum','Lyngby','Gentofte','Virum','Holte','Nærum','Dyssegård','Bagsværd',
			'Hellerup','Charlottenlund','Klampenborg','Skodsborg','Vedbæk','Rungsted','Hørsholm',
			'Kokkedal','Nivå','Helsingør','Humlebæk','Espergærde','Snekkersten','Tikøb','Hornbæk',
			'Dronningmølle','Ålsgårde','Hellebæk','Helsinge','Vejby','Tisvildeleje','Græsted','Gilleleje',
			'Frederiksværk','Ølsted','Skævinge','Gørløse','Liseleje','Melby','Hundested','Hillerød',
			'Allerød','Birkerød','Fredensborg','Kvistgård','Værløse','Farum','Lynge','Slangerup',
			'Frederikssund','Jægerspris','Ølstykke','Stenløse','Veksø','Skibby']

df = read_csv("../csv/crime.csv", sep=";", names=categories)
for item in categories[1:-1]:
	df[item] = df[item].str.replace('\'','').astype(int)

for i in range(len(df['date'])):
	for month in months:
		if month in str(df['date'][i]):
			df.loc[i,'date']= monthAverage*(months.index(month)+1)

#print(df['date'])

#df = df[df['city']=='hillerød']

# DET HER ER NYT
for i in range(len(cityNames)):
	df = DataFrame(df.loc[df['city'].str.contains(cityNames[i],case=False)])
	print(df)
	print(df[["date","severity"]])
	clus = 12
	if df['city'].count() < 12:
		clus = 1
	print(df[["date","severity"]])

	kmeans = KMeans(n_clusters=clus).fit(df[["date","severity"]])
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

	plt.title(label=cityNames[i].capitalize())
	plt.scatter(df['date'], df['severity'], s=50, alpha=0.5, c= kmeans.labels_.astype(float))
	plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
	plt.xlabel("Date")
	plt.ylabel("Severity")

	plt.savefig("../img/"+cityNames[i]+".png",)
	#plt.show()
	plt.close()#  Den her behøver vi måske ikke nødvendigvis, det er bare pænest
