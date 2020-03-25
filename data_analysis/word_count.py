import json
import glob

countsDict = {}

def word_count():
	data = ""
	files = glob.glob("../page_content/*.txt")

	for i in range(len(files)):
		with open(files[i], encoding='utf8') as file:
			temp = file.read().replace("\n"," ")
			data += temp
		file.close()

	words = data.split()

	for word in words:  #Looper igennem ord i den splittede string
		if word in countsDict:
			countsDict[word] += 1  #Hvis ordet eksisterer sæt antal 1 op 
		else:
			countsDict[word] = 1  #Ellers tilføj ord med værdien 1

	#Konverter dict til json
	with open ("word_count.json","w") as out:
		out.write(json.dumps(countsDict))
	return countsDict

word_count()

sorted_dict=sorted(countsDict.items(), key=lambda x: x[1])
for item in sorted_dict:
	print(item)


