# -*- coding: utf-8 -*-

from pandas import DataFrame, read_csv, to_numeric
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import json
from csv_to_json import csv_json

months = ['januar', 'februar', 'marts','april','maj','juni','juli','august','september','oktober','november','december']
categories = ["date","driving","drugs","lethal","other","stealing","violence","severity","city"]

monthAverage = 100000000000#30.4368499

cityNames = ['Ballerup','Gentofte','Lyngby','Smørum','Virum','Holte','Nærum','Dyssegård','Bagsværd',
			'Hellerup','Charlottenlund','Klampenborg','Skodsborg','Vedbæk','Rungsted','Hørsholm',
			'Kokkedal','Nivå','Helsingør','Humlebæk','Espergærde','Snekkersten','Tikøb','Hornbæk',
			'Dronningmølle','Ålsgårde','Hellebæk','Helsinge','Vejby','Tisvildeleje','Græsted','Gilleleje',
			'Frederiksværk','Ølsted','Skævinge','Gørløse','Liseleje','Melby','Hundested','Hillerød',
			'Allerød','Birkerød','Fredensborg','Kvistgård','Værløse','Farum','Lynge','Slangerup',
			'Frederikssund','Jægerspris','Ølstykke','Stenløse','Veksø','Skibby']

csv_json()
with open('../csv/cities.json',encoding='utf-8') as f:
	data = json.load(f)

for z in range(len(cityNames)):

	df = read_csv("../csv/crime.csv", sep=";", names=categories)
	for item in categories[1:-1]:
		df[item] = df[item].str.replace('\'','').astype(int)

	for i in range(len(df['date'])):
		for month in months:
			if month in str(df['date'][i]):
				df.loc[i,'date']= monthAverage*(months.index(month)+1)

	df = DataFrame(df.loc[df['city'].str.contains(cityNames[z],case=False)])
	print(cityNames[z],str(z+1)+"/"+str(len(cityNames)))
	clus = 12
	if df['city'].count() < 12:
		clus = df['city'].count()
	
	
	kmeans = KMeans(n_clusters=clus).fit(df[["date","severity"]])
	centroids = kmeans.cluster_centers_

	averageList = []
	for item in centroids:
		averageList.append(item[1])
	average = sum(averageList)/12
	
	a = data[cityNames[z].lower()] 
	a.append(average)
	imageLink = open('../csv/imgLink.txt', 'r').readlines()
	a.append(imageLink[z].strip())
	data[cityNames[z]] = a    

	with open('../csv/cities.json', 'w',encoding='utf-8') as f:
		json.dump(data,f)
		f.close()

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

