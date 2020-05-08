from pandas import DataFrame, read_csv, to_numeric
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import json
from csv_to_json import csv_json

# Plot og gem grafer
def plotGraph():
	ticks = []
	for i in range(1,13):
		ticks.append(monthAverage*i)
	labels = ['Jan', 'Feb', 'Mar', 'Apr','Maj','Jun','Jul','Aug','Sep','Okt','Nov','Dec']

	plt.figure()
	plt.axhline(average,0,10000000,color='purple')
	plt.xticks(ticks, labels,rotation=20)

	plt.title(label=cityNames[z].capitalize())
	plt.scatter(df['date'], df['severity'], s=50, alpha=0.5, c= kmeans.labels_.astype(float))
	plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
	plt.xlabel("Date")
	plt.ylabel("Severity")

	plt.savefig("../img/"+cityNames[z]+"_"+str(clus)+".png")
	plt.close()

# Liste med måneder, kategorier til pandas DataFrame, byer
months = ['januar', 'februar', 'marts','april','maj','juni','juli','august','september','oktober','november','december']
categories = ["date","driving","drugs","lethal","other","stealing","violence","severity","city"]

cityNames = ['Ballerup','Smørum','Lyngby','Gentofte','Virum','Holte','Nærum','Dyssegård','Bagsværd',
			'Hellerup','Charlottenlund','Klampenborg','Skodsborg','Vedbæk','Rungsted','Hørsholm',
			'Kokkedal','Nivå','Helsingør','Humlebæk','Espergærde','Snekkersten','Tikøb','Hornbæk',
			'Dronningmølle','Ålsgårde','Hellebæk','Helsinge','Vejby','Tisvildeleje','Græsted','Gilleleje',
			'Frederiksværk','Ølsted','Skævinge','Gørløse','Liseleje','Melby','Hundested','Hillerød',
			'Allerød','Birkerød','Fredensborg','Kvistgård','Værløse','Farum','Lynge','Slangerup',
			'Frederikssund','Jægerspris','Ølstykke','Stenløse','Veksø','Skibby']

# Variabel til seperering af måneder
monthAverage = 100000000000#30.4368499

# Kører funktion fra csv_to_json.py
csv_json()

# Henter json fil med data fra byer
with open('../data_files/cities.json',encoding='utf-8') as f:
	data = json.load(f)

# Åbner csv og formaterer det til en DataFrame 
dfStatic = read_csv("../data_files/crime.csv", sep=";", names=categories)
for item in categories[1:-1]:
	dfStatic[item] = dfStatic[item].str.replace('\'','').astype(int)

# Looper igennem alle byer, laver clustering og gemmer data i json
for z in range(len(cityNames)):
	df = dfStatic 

	# Isolerer alle måneder så de hver kan repræsenteres af et cluster
	for i in range(len(df['date'])):
		for month in months:
			if month in str(df['date'][i]):
				df.loc[i,'date']= monthAverage*(months.index(month)+1)

	# Valg af byer fra DataFrame, antal clusters, clustering og definering af centroids
	df = DataFrame(df.loc[df['city'].str.contains(cityNames[z],case=False)])
	print(cityNames[z],str(z+1)+"/"+str(len(cityNames)))
	clus = 12
	if df['city'].count() < 12:
		clus = df['city'].count()		
	kmeans = KMeans(n_clusters=clus).fit(df[["date","severity"]])
	centroids = kmeans.cluster_centers_

	# Gennemsnit for centroids
	averageList = []
	for item in centroids:
		averageList.append(item[1])
	average = sum(averageList)/12
	
	# Værdier der skal bruges på hjemmeside tilføjes til json, først gennemsnit for centroids
	a = data[cityNames[z].lower()]
	a.append(average)
	# Værdier for alle kategorier tilføjes som brøkdel af det samlede gennemsnit
	df = df.reset_index()
	with open('../data_files/weight.json', 'r', encoding='utf8') as weight:
		wDict = json.load(weight)
		L_pSum = [0,0,0,0,0,0]
		for y in range(1,7):  #categories 1-6 [.."driving","drugs","lethal","other","stealing","violence"..]
			pSum = 0
			for x in range(len(df[categories[y]])):
				if df.at[x,categories[y]]:
					pSum+=1
			pSum *= wDict[categories[y]]
			L_pSum[y-1] = pSum
		for item in L_pSum:
			a.append(item/sum(L_pSum) * average)

	# Ling til grafer
	imageLink = open('../data_files/imgLink.txt', 'r').readlines()
	a.append(imageLink[z].strip())
	data[cityNames[z].lower()] = a

	# y-værdier for enkelte clusters tilføjes, så de kan plottes på en graf på hjemmesiden
	y_values = [0,0,0,0,0,0,0,0,0,0,0,0]
	for v in range(int(centroids.size/2)):
		y_values[int(round(centroids[v,0]/monthAverage))-1] = round(centroids[v,1],2)
	a.append(y_values)

	# Json bliver opdateret, med de nye værdier
	with open('../data_files/cities.json', 'w',encoding='utf-8') as f:
		json.dump(data,f)
		f.close()

	# Plot graf kaldes
	plotGraph()

