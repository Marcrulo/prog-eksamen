import csv, json

def csv_json():
	outputDict = {}

	# konverterer en del af regionsopdelt_postnummer.csv til json: Byer, koordinater, population
	with open('../data_files/regionsopdelt_postnummer.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
		next(reader)
		for row in reader:
			a = row[5].lower()
			outputDict[a] = [row[6],row[7],row[8]]

	with open ("../data_files/cities.json","w", encoding='utf8') as out:
		json.dump(outputDict,out, ensure_ascii=False)

	print(outputDict)

# csv_json kaldes externt, men hvis filen skal køres manuelt skal følgende anvendes
if __name__ == '__main__':
	csv_json()
