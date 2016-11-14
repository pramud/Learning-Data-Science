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


#BUILDING TRAINING DATA 

#After importing the
#dataset, we will randomly select about 75 percent of the instances, and reserve the
#remaining ones (the evaluation dataset) for evaluation purposes

from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
# Get dataset with only the first two attributes
X, y = X_iris[:, :2], y_iris
# Split the dataset into a training and a testing set
# Test set will be the 25% taken randomly
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
print X_train.shape, y_train.shape (112, 2) (112,)
# Standardize the features
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

'''The train_test_split function automatically builds the training and evaluation
datasets, randomly selecting the samples. Why not just select the first 112 examples?
This is because it could happen that the instance ordering within the sample could
matter and that the first instances could be different to the last ones. In fact, if you
look at the Iris datasets, the instances are ordered by their target class, and this
implies that the proportion of 0 and 1 classes will be higher in the new training set,
compared with that of the original dataset. We always want our training data to be a
representative sample of the population they represent.'''

'''The last three lines of the previous code modify the training set in a process usually
called feature scaling. For each feature, calculate the average, subtract the mean
value from the feature value, and divide the result by their standard deviation. After
scaling, each feature will have a zero average, with a standard deviation of one. This
standardization of values (which does not change their distribution, as you could
verify by plotting the X values before and after scaling) is a common requirement of
machine learning methods, to avoid that features with large values may weight too
much on the final results.'''

#PLOTTING

import matplotlib.pyplot as plt
colors = ['red', 'greenyellow', 'blue']
for i in xrange(len(colors)):
  xs = X_train[:, 0][y_train == i]
  ys = X_train[:, 1][y_train == i]
  plt.scatter(xs, ys, c=colors[i])
plt.legend(iris.target_names)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
