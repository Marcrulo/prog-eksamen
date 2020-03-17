#import pandas as pd
#df = pd.read_excel('https://query.data.world/s/zxntjvkrukw2mzranhido7arraqr6c')

import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split#, cross_validation
from sklearn.neighbors import KNeighborsClassifier

# csv to numpy
from numpy import genfromtxt
train = genfromtxt('IdeologyStats.csv', delimiter=',')

race = genfromtxt('data/race.csv', delimiter=',')
religion = genfromtxt('data/religion.csv', delimiter=',')
income = genfromtxt('data/income.csv', delimiter=',')
education = genfromtxt('data/education.csv', delimiter=',')
age = genfromtxt('data/age.csv', delimiter=',')
ideology = genfromtxt('data/ideology.csv', delimiter=',')



X_train, X_test, y_train, y_test = train_test_split(train, ideology)

knn = KNeighborsClassifier(n_neighbors=1)



knn.fit(X_train, y_train)



plt.scatter(education,income, c=ideology)
plt.xlabel("education")
plt.ylabel("income")

plt.show()

race = {
	1 : 'White non-Hispanic',
	2 : 'Black non-HIspanic',
	3 : 'Hispanic',
	4 : 'Other non-Hispanic'
}

religion = {
	0 : 'Important',
	1 : 'Not important'
}

family_income = {
	1 : 'Under $5,000',
	2 : '$5,000-$9,999',
	3 : '$10,000-$12,499',
	4 : '$12,500-$14,999',
	5 : '$15,000-$17,499',
	6 : '$17,500-$19,999',
	7 : '$20,000-$22,499',
	8 : '$22,500-$24,999',
	9 : '$25,000-$27,499',
	10 : '$27,500-$29,999',
	11 : '$30,000-$34,999',
	12 : '$35,000-$39,999',
	13 : '$40,000-$44,999',
	14 : '$45,000-$49,999',
	15 : '$50,000-$54,999',
	16 : '$55,000-$59,999',
	17 : '$60,000-$64,999',
	18 : '$65,000-$69,999',
	19 : '$70,000-$74,999',
	20 : '$75,000-$79,999',
	21 : '$80,000-$89,999',
	22 : '$90,000-$99,999',
	23 : '$100,000-$109,999',
	24 : '$110,000-$124,999',
	25 : '$125,000-$149,999',
	26 : '$150,000-$174,999',
	27 : '$175,000-$249,999',
	28 : '$250,000 or more',
}

education = {
	1 : 'Less than high school credential',
	2 : 'High school credential',
	3 : 'Some post-high-school, no bachelor\'s degree',
	4 : 'Bachelor\'s degree',
	5 : 'Graduate degree',
}

age_group = {
	1 : '17-20',
	2 : '21-24',
	3 : '25-29',
	4 : '30-34',
	5 : '35-39',
	6 : '40-44',
	7 : '45-49',
	8 : '50-54',
	9 : '55-59',
	10 : '60-64',
	11 : '65-69',
	12 : '70-74',
	13 : '>=75'
}

Ideology = {
	1 : 'Extremely liberal',
	2 : 'Liberal',
	3 : 'Slightly liberal',
	4 : 'Moderate; middle of the road',
	5 : 'Slightly conservative',
	6 : 'Conservative',
	7 : 'Extremely conservative'
}