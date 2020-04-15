import csv
import glob


csvfile = open('crime.csv', "w", encoding='utf-8',newline="")
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
				
			id = file.replace('../page_content\\','') + '#' + str(points['index'])
			writer.writerow([id,points['driving'],points['drugs'],points['lethal'],points['other'],points['stealing'],points['violence']])			

	txtfile.close()



