import requests
import csv
import glob


def compareKeyword():
	pass

def loopSection():
	compareKeyword() # Sammenlign hvert ord med keywordlist, 
					 # og tilføj 1 til hvert kategori, 
					 # hvis der er relevant ord


# Write to CSV file
csvfile = open('crime.csv', "w", encoding='utf-8',newline="")
files = glob.glob("../page_content/*.txt")


points = {
	'driving' : 0,
	'drugs'   : 0,
	'lethal'  : 0,
	'other'   : 0,
	'stealing': 0,
	'violence': 0
}

for file in files:
	with open(file, encoding='utf8') as file:
		loopSection() # Loop gennem afsnit 
	file.close()


writer = csv.writer(csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_ALL)

