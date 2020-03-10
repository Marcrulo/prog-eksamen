import requests # Make URL requests
from bs4 import BeautifulSoup # Filter through fetched HTML-code
import json

URL = "http://www.tageo.com/index-e-da-cities-DK.htm"
# http://www.tageo.com/index-e-da-cities-DK-step-1.htm
# http://www.tageo.com/index-e-da-cities-DK-step-2.htm
# http://www.tageo.com/index-e-da-cities-DK-step-3.htm
# http://www.tageo.com/index-e-da-cities-DK-step-4.htm

# Get HTML as text
page = requests.get(URL)

# Create soup object, which makes it possible to filter the HTML 
soup = BeautifulSoup(page.content, "html.parser")

# Filter/find div by class name. Returns entire tags
content = soup.find("table", {"class": "V2"})
data = content.findAll("tr")

city_dict = {}
for d in data[1:]:
	a = d.findAll('td')
	city_dict['name'] = 
	city_dict[a[1].text.strip()] = [a[0].text.strip(),a[2].text.strip(),a[3].text.strip()] #ID


print(city_dict)
'''
city_dict = {
	city_name = [id, latitude, longitude]	
}

'''


with open('cities.json', 'a') as json_file:
	json.dump(city_dict, json_file)

