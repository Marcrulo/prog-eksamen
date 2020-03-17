import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

import numpy as np

# iris dataset
iris = load_iris()
print(iris.data)

# split data 
X_train, X_test, Y_train, Y_test = train_test_split(iris['data'], iris['target'], random_state=0)

# classifier class
knn = KNeighborsClassifier(n_neighbors=1)

# ---
knn.fit(X_train, Y_train)

# ---
X_new = np.array([[5.0, 2.9, 1.0, 0.2]])

#prediction = knn.predict(X_new)
#print(prediction)

# model accuracy
#print(knn.score(X_test, Y_test))



