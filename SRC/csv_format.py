#Make proper csv format

import csv

'''
race
religion
income
education
age
ideology
'''


with open('data/ideology.csv', 'w', newline='') as myFile:
	writer = csv.writer(myFile)
	

	with open('IdeologyStats.csv', 'r', newline='') as File:  
		reader = csv.reader(File)
		for row in reader:
			try:
				if 1 <= int(row[5]) <= 3:
					ideo = 0
				elif int(row[5]) == 4:
					ideo = 0
				else:
					ideo = 1
				
				shortened = [
					ideo
				]

			
			#try:
			#	if row[3].isdigit():
			#		shortened = [
			#				int(row[1][0]),
			#				int(row[2][0]),
			#				int(row[3]),
			#				int(row[4][0]),
			#				int(row[5][0]),
			#				int(row[6][0]),
			#			]
			#	else:
			#		print('næ')
			#		continue
			

			except:
				print('skip')
				continue

			writer.writerow(shortened)

		File.close()
	myFile.close()
