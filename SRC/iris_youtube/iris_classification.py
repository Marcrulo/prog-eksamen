
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# iris dataset
iris = load_iris()

# dataset split in features
features = iris.data.T

# list of features
sepal_length = features[0]
sepal_width = features[1]
petal_length = features[2]
petal_width = features[3]

# name of features
sepal_length_label = iris.feature_names[0]
sepal_width_label = iris.feature_names[1]
petal_length_label = iris.feature_names[2]
petal_width_label = iris.feature_names[3]

# scatterplot
# arg1 = x; arg2 = y; c = mark each class/target with a color    
plt.scatter(sepal_length, sepal_width, c=iris.target)
plt.xlabel("Sepal Length")
plt.ylabel("Speal Width")
plt.show()










