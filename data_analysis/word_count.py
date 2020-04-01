import json
import glob

countsDict = {}

def word_count():
	data = ""
	files = glob.glob("../page_content/*.txt")

	for i in range(len(files)):
		with open(files[i], encoding='utf8') as file:
			data += file.read().replace("\n"," ")
		file.close()


	words = data.lower().split()
	
	for word in words:  #Looper igennem ord i den splittede string
		symbols = ['.',',',';',':','!','?'] #hvis der dukkker gentagelser af ord op i json, skal flere symboler evt tilføjes
		if word[-1] in symbols and word[-2].isnumeric() is False:
			word = word[:-1]

		if word in countsDict:
			countsDict[word] += 1  #Hvis ordet eksisterer sæt antal 1 op 
		else:
			countsDict[word] = 1  #Ellers tilføj ord med værdien 1

	#Konverter dict til json
	with open ("word_count.json","w", encoding='utf8') as out:
		json.dump(countsDict,out, ensure_ascii=False)
	return countsDict

word_count()

#sorted_dict=sorted(countsDict.items(), key=lambda x: x[1])
#for item in sorted_dict:
	#print(item)

