import csv
import glob
import json


csvfile = open('../data_files/crime.csv', "w", encoding='utf-8',newline="")
writer = csv.writer(csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_ALL)
files = glob.glob("../page_content/*.txt")

for file in files: # Files in PAGE_CONTENT
	with open(file, encoding='utf8') as txtfile: # %DAY% %MONTH% %YEAR%.txt
		
		a = txtfile.read().split('\n\n') # Split into seperate sections
		for i in range(len(a)): # Loop through SECTIONS first time
			
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

			for sec in section: # Normalising and data formatting
				symbols = ['.',',',';',':','!','?']
				if(len(sec)-1):  
					if sec[-1] in symbols and sec[-2].isnumeric() is False:
						sec = sec[:-1]
			
			
				
			for word in section: # Loop through SECTIONS second time to compare with keywords 
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

			### TODO ###
			'''
				1) Extract city name
				2) Exclude sections with weird formatting
				3) Specific tid/dato
				4) New column which contains each parameter times its severity
			'''

			id = file.replace('../page_content\\','') + '#' + str(points['index'])

			with open('../data_files/weight.json', 'r', encoding='utf8') as weight:
				wDict = json.load(weight)
				categoryList = ['driving','drugs','lethal','other','stealing','violence']
				pList = [points['driving'],points['drugs'],points['lethal'],points['other'],points['stealing'],points['violence']]
				pointSum = 0
				for i in range(len(pList)):
					if pList[i]:
						pointSum += wDict[categoryList[i]]

				#pointSum = points['driving']*wDict['driving'] + points['drugs']*wDict['drugs'] + points['lethal']*wDict['lethal'] + points['other']*wDict['other'] + points['stealing']*wDict['stealing'] + points['violence']*wDict['violence']
				#print(pointSum)

				writer.writerow([id,points['driving'],points['drugs'],points['lethal'],points['other'],points['stealing'],points['violence'],pointSum,crimeCity])			
				print(points['driving'],points['drugs'],points['lethal'],points['other'],points['stealing'],points['violence'],pointSum,crimeCity)

	txtfile.close()



