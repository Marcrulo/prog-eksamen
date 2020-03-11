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

	
day2 = i+1