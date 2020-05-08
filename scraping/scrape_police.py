import requests 
import re
from bs4 import BeautifulSoup 

def line_empty(line):
    return len(line.strip()) < 1

# Søgekriterier
fromDate = "2019/4/12" # År/Månded/Dag
toDate = "2020/4/12"   # År/Månded/Dag
page = 11 			   # Sider vælges manuelt, så vi ikke overskrider "request limit"

URL = "https://politi.dk/doegnrapporter?fromDate={}&toDate={}&newsType=D%C3%B8gnrapporter&page={}&district=Nordsjaellands-Politi".format(fromDate,toDate,page)
print(URL)

# Find sider baseret på søgekriterier
frontPage = requests.get(URL)
soup = BeautifulSoup(frontPage.content, "html.parser")
ngCtrl = soup.find('section', {'ng-controller': 'newsListController'})
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(ngCtrl))
if len(urls) == 0:
	print("End reached")

# Gem Sidernes indhold
for url in urls:	
	subPage = requests.get(url)
	bs = BeautifulSoup(subPage.content, "html.parser")

	content = bs.find("div", {"class": "rich-text"})
	date = bs.find_all('p',{'class':'newsInfoText body-xmedium-police-regular dark-blue'})[1].text.strip()

	file = open("../page_content/{}.txt".format(date), "w", encoding="UTF-8")

	lines = content.text.strip().split('\n') 
	for line in lines:
		if not line.startswith("Indbrud i privat beboelse anmeldt til Nordsjællands Politi"):	
			file.write(line+'\n')

	file.close()
	