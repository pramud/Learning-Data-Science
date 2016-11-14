import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
iris = datasets.load_iris()
X_iris, y_iris = iris.data, iris.target

print X_iris.shape, y_iris.shape
print X_iris[0], y_iris[0]
