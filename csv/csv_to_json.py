

import csv, json


outputDict = {}

with open('regionsopdelt_postnummer.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=';')
	next(reader)
	for row in reader:
		a = row[5].lower()
		outputDict[a] = [row[6],row[7],row[8]]



with open ("cities.json","w", encoding='utf8') as out:
	json.dump(outputDict,out, ensure_ascii=False)

print(outputDict)


