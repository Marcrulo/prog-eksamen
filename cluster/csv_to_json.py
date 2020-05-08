

import csv, json

def csv_json():
	outputDict = {}

	with open('../csv/regionsopdelt_postnummer.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		next(reader)
		for row in reader:
			a = row[5].lower()
			outputDict[a] = [row[6],row[7],row[8]]



	with open ("../csv/cities.json","w", encoding='utf8') as out:
		json.dump(outputDict,out, ensure_ascii=False)

	print(outputDict)

if __name__ == '__main__':
	csv_json()
