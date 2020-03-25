import requests # Make URL requests
import re
from bs4 import BeautifulSoup # Filter through fetched HTML-code

def line_empty(line):
    return len(line.strip()) < 1

# Search criteria
fromDate = "2020/1/15" # Year/Month/Day
toDate = "2020/2/15"  # Year/Month/Day
page = 1 			  # Page ... pages are done manually due to risks of request limit

URL = "https://politi.dk/doegnrapporter?fromDate={}&toDate={}&newsType=D%C3%B8gnrapporter&page={}&district=Nordsjaellands-Politi".format(fromDate,toDate,page)

# Find pages based on search criteria
frontPage = requests.get(URL)
soup = BeautifulSoup(frontPage.content, "html.parser")
ngCtrl = soup.find('section', {'ng-controller': 'newsListController'})
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(ngCtrl))
if len(urls) == 0:
	print("End reached")

# Save page content
for url in urls:	
	subPage = requests.get(url)
	bs = BeautifulSoup(subPage.content, "html.parser")

	content = bs.find("div", {"class": "rich-text"})
	date = bs.find_all('p',{'class':'newsInfoText body-xmedium-police-regular dark-blue'})[1].text.strip()

	file = open("../page_content/{}.txt".format(date), "w", encoding="UTF-8")

	lines = content.text.strip().split('\n') 
	for line in lines:
	    file.write(line+'\n')

	file.close()
	

# Extract relevant data from content


