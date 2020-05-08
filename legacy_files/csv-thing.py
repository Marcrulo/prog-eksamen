import requests
import csv

# Open content file
file = open('tmpfile.txt', encoding='UTF-8')

# Write to CSV file
csvfile = open('tmpfile.csv', "w", encoding='utf-8',newline="")
writer = csv.writer(csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_ALL)

''' Filtrer vigtig viden, og indsæt i csv fil '''
''' Data auditing i csv fil (program til at checke om data opfylder det rigtige format) '''


