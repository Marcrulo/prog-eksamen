import requests # Make URL requests
from bs4 import BeautifulSoup # Filter through fetched HTML-code


def line_empty(line):
    return len(line.strip()) < 1


BASE_URL = "https://politi.dk/nordsjaellands-politi/doegnrapporter/uddrag-af-doegnrapport"


month = "februar"
month_index = '02' # Inkluder 0 (fx 02, 03, 10, 11)
days = 29
year = 2020

for i in range(days-1):
	
	if i < 10:
		day1 = "0"+str(i)
		if i+1 < 10:
			day2 = "0"+str(i+1)
	else:
		day1 = i
		day2 = i+1
	
	 

	URL = BASE_URL + "-{0}{1}-{2}-{3}/{3}/{4}/{1}".format(day1,day2,month,year,month_index)
	print(URL)

	
	# Get HTML as text
	page = requests.get(URL)

	# Create soup object, which makes it possible to filter the HTML 
	soup = BeautifulSoup(page.content, "html.parser")

	# Filter/find div by class name. Returns entire tags
	content = soup.find("div", {"class": "rich-text"})

	# Strips the text from the tags
	print(content.text.strip())


	# Find the second p-tag with the certain class. This returns a date 
	Dato = soup.findAll("p", {"class": "newsInfoText body-xmedium-police-regular dark-blue"})[1]
	txt = Dato.text.strip()
	print(txt)


	''' Put content in txt-file '''
	# Write to txt-file
	file = open("tmpfile{}.txt".format(str(day1)+str(day2)), "w", encoding="UTF-8")

	# Seperate content section by newline
	lines = content.text.strip().split('\n')
	for line in lines:
	    if not line_empty(line):
	        file.write(line+'\n')
	file.close()