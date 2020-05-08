import csv
import glob
import json

# Åbner scrapet data og skriver til crime.csv
csvfile = open('../data_files/crime.csv', "w", encoding='utf-8',newline="")
writer = csv.writer(csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_ALL)
files = glob.glob("../page_content/*.txt")

# alle filer kigges igennem, hvor en iteration svarer til en dags døgnrapport
for file in files:
	with open(file, encoding='utf8') as txtfile: # %DAY% %MONTH% %YEAR%.txt
		
		#Laver en liste af tekst som sektioner af døgnrapporten (et item = en sektion/forbrydelse)
		a = txtfile.read().split('\n\n') 
		for i in range(len(a)): 
			
			points = {
				'driving' : 0,
				'drugs'   : 0,
				'lethal'  : 0,
				'other'   : 0,
				'stealing': 0,
				'violence': 0,
				'index'   : i,
			}
			section = a[i].lower().split()

			# Normalisering og formatering af data
			for sec in section: 
				symbols = ['.',',',';',':','!','?']
				if(len(sec)-1):  
					if sec[-1] in symbols and sec[-2].isnumeric() is False:
						sec = sec[:-1]
			
			
			# Looper igennem sektioner og alle ord sammenlignes med keywords 	
			for word in section: 
				with open('../keywordlists/driving.txt', encoding='utf-8') as driving:		
					for keyword in driving.read().split('\n'):
						if word.startswith(keyword):
							points['driving'] += 1
							

				with open('../keywordlists/drugs.txt', encoding='utf-8') as drugs:
					for keyword in drugs.read().split('\n'):
						if word.startswith(keyword):
							points['drugs'] += 1
							

				with open('../keywordlists/lethal.txt', encoding='utf-8') as lethal:
					for keyword in lethal.read().split('\n'):
						if word.startswith(keyword):
							points['lethal'] += 1
							

				with open('../keywordlists/other.txt', encoding='utf-8') as other:
					for keyword in other.read().split('\n'):
						if word.startswith(keyword):
							points['other'] += 1
							

				with open('../keywordlists/stealing.txt', encoding='utf-8') as stealing:
					for keyword in stealing.read().split('\n'):
						if word.startswith(keyword):
							points['stealing'] += 1
							

				with open('../keywordlists/violence.txt', encoding='utf-8') as violence:
					for keyword in violence.read().split('\n'):
						if word.startswith(keyword):
							points['violence'] += 1

				
				with open('../keywordlists/city.txt', encoding='utf-8') as city:
					for keyword in city.read().split('\n'):
						if word.startswith(keyword):
							crimeCity = keyword
							break


			# Gem data i csv
			id = file.replace('../page_content\\','') + '#' + str(points['index'])
			with open('../data_files/weight.json', 'r', encoding='utf8') as weight:
				wDict = json.load(weight)
				categoryList = ['driving','drugs','lethal','other','stealing','violence']
				pList = [points['driving'],points['drugs'],points['lethal'],points['other'],points['stealing'],points['violence']]
				pointSum = 0
				for i in range(len(pList)):
					if pList[i]:
						pointSum += wDict[categoryList[i]]

				writer.writerow([id,points['driving'],points['drugs'],points['lethal'],points['other'],points['stealing'],points['violence'],pointSum,crimeCity])			
				print(points['driving'],points['drugs'],points['lethal'],points['other'],points['stealing'],points['violence'],pointSum,crimeCity)

	txtfile.close()
