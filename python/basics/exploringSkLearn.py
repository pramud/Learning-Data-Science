import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()
X_iris, y_iris = iris.data, iris.target

print X_iris.shape, y_iris.shape
print X_iris[0], y_iris[0]

#iris dataset is an object (similar to a dictionary) that has two main components

#A data array, where, for each instance, we have the real values for sepal
#length, sepal width, petal length, and petal width, in that order (note that for
#efficiency reasons, scikit-learn methods work on NumPy ndarrays instead of
#the more descriptive but much less efficient Python dictionaries or lists). The
#shape of this array is (150, 4), meaning that we have 150 rows (one for each
#instance) and four columns (one for each feature).

#A target array, with values in the range of 0 to 2, corresponding to each
#instance of Iris species (0: setosa, 1: versicolor, and 2: virginica), as you can
#verify by printing the iris.target.target_names value.

