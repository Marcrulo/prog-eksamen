import requests # Make URL requests
import re
from bs4 import BeautifulSoup # Filter through fetched HTML-code


def line_empty(line):
    return len(line.strip()) < 1


'''
https://politi.dk/doegnrapporter
?fromDate=2020/2/1
&toDate=2020/2/29
&newsType=D%C3%B8gnrapporter
&page=1
&district=Nordsjaellands-Politi
'''

fromDate = "2020/2/1" # Year/Month/Day
toDate = "2020/2/29"  # Year/Month/Day
URL = "https://politi.dk/doegnrapporter?fromDate={}&toDate={}&newsType=D%C3%B8gnrapporter&page={}&district=Nordsjaellands-Politi".format(fromDate,toDate,1)

#print(URL)

frontPage = requests.get(URL)
soup = BeautifulSoup(frontPage.content, "html.parser")

ngCtrl = soup.find('section', {'ng-controller': 'newsListController'})
#print(ngCtrl)

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(ngCtrl))
for url in urls:
	print(url)
'''
file = open("FRONTPAGE.html",'w',encoding="UTF-8")
file.write(str(ngCtrl))

links = soup.find_all("a", {"class": "newsResultLink"})
'''





'''
linksAvailable = True
page = 1
while linksAvailable:
	pass
'''










'''
# Get HTML as text
page = requests.get(URL)

# Create soup object, which makes it possible to filter the HTML 
soup = BeautifulSoup(page.content, "html.parser")

print(soup.title.text)
if soup.title.text == "Runtime":
	print("Runtime Error!!!\n") 


# Filter/find div by class name. Returns entire tags
content = soup.find("div", {"class": "rich-text"})

# Strips the text from the tags
#print(content.text.strip())


# Find the second p-tag with the certain class. This returns a date 
Dato = soup.findAll("p", {"class": "newsInfoText body-xmedium-police-regular dark-blue"})[1]
txt = Dato.text.strip()
#print(txt)


# Put content in txt-file
# Write to txt-file
file = open("tmpfile{}.txt".format(str(day1)+str(day2)), "w", encoding="UTF-8")

# Seperate content section by newline
lines = content.text.strip().split('\n')
for line in lines:
    if not line_empty(line):
        file.write(line+'\n')
file.close()
'''
