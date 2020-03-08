import requests # Make URL requests
from bs4 import BeautifulSoup # Filter through fetched HTML-code

# 
def line_empty(line):
    return len(line.strip()) < 1


URL = "https://politi.dk/oestjyllands-politi/doegnrapporter/doegnrapport-fra-oestjyllands-politi-onsdag-den-26-februar-2020/2020/02/26"

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
file = open("tmpfile.txt", "w", encoding="UTF-8")

# Seperate content section by newline
lines = content.text.strip().split('\n')
for line in lines:
    if not line_empty(line):
        file.write(line+'\n')
file.close()
