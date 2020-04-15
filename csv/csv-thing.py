import requests
import csv

# Open content file
file = open('tmpfile.txt', encoding='UTF-8')

# Write to CSV file
csvfile = open('tmpfile.csv', "w", encoding='utf-8',newline="")
writer = csv.writer(csvfile, delimiter=';', quotechar="'", quoting=csv.QUOTE_ALL)

''' Filtrer vigtig viden, og indsæt i csv fil '''
''' Data auditing i csv fil (program til at checke om data opfylder det rigtige format) '''



''' USELESS, JUST IGNORE
row = [';', ';', ';', ';', ';']
pattern = "[0-9][0-9].[0-9][0-9]"
pattern_alder = "[0-9][0-9]-årig"


while True:
    line = file.readline()
    row[0] = line.strip()
    line = file.readline()
    row[1] = line.strip()
    row[2] = line.strip().split(':')[0]

    # Her skal vi udtrække data og lægge i row-listen
    writer.writerow(row)
    if not line:
        break
file.close()
'''