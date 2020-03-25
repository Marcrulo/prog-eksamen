import json


countsDict = {}
def word_count(str):
    words = str.split()

    for word in words:  #Looper igennem ord i den splittede string
        if word in countsDict:
            countsDict[word] += 1  #Hvis ordet eksisterer sæt antal 1 op 
        else:
            countsDict[word] = 1  #Ellers tilføj ord med værdien 1

    countsJson = json.dumps(countsDict)  #Konverter dict til json
    return countsDict

with open("../page_content/16-17-2020.txt") as file:
	data = file.read().replace("\n","")

word_count(data)
sorted_dict=sorted(countsDict.items(), key=lambda x: x[1])
#print(sorted_dict)
for item in sorted_dict:
	print(item)