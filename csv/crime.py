import requests
import csv
import glob


# Write to CSV file
csvfile = open('crime.csv', "w", encoding='utf-8',newline="")
files = glob.glob("../page_content/*.txt")

points = {
	'driving' : 0,
	'drugs'   : 0,
	'lethal'  : 0,
	'other'   : 0,
	'stealing': 0,
	'violence': 0,
	'index'   : 0,
}

for file in files:
	with open(file, encoding='utf8') as txtfile:
		
		a = txtfile.read().split('\n\n')
		for item in a:
			print(item)
			print("----")

		# Loop gennem afsnit 
		#    reset point
		#    For hvert afsnit:
		#       loop gennem keywordlists
		#          tilføj point
		#          writer = csv.writer(csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_ALL)



	txtfile.close()




