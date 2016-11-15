import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
faces = fetch_olivetti_faces()
print faces.DESCR

'''Looking at the content of the faces object, we get the following properties: images,
data, and target. Images contain the 400 images represented as 64 x 64 pixel
matrices. data contains the same 400 images but as array of 4096 pixels. target is, as
expected, an array with the target classes, ranging from 0 to 39'''

print faces.keys()
print faces.images.shape
print faces.data.shape
print faces.target.shape

'''Normalizing the data is important as we saw in the previous chapter. It is also
important for the application of SVM to obtain good results. In our particular case,
we can verify by running the following snippet that our images already come as
values in a very uniform range between 0 and 1 (pixel value):'''

print np.max(faces.data)
print np.min(faces.data)
print np.mean(faces.data)

'''Therefore, we do not have to normalize the data. Before learning, let's plot some
faces. We will define the following helper function:'''

def print_faces(images, target, top_n):
  # set up the figure size in inches
  fig = plt.figure(figsize=(12, 12))
  fig.subplots_adjust(left=0, right=1, bottom=0, top=1,hspace=0.05, wspace=0.05)
  for i in range(top_n):
    # plot the images in a matrix of 20x20
    p = fig.add_subplot(20, 20, i + 1, xticks=[],yticks=[])
    p.imshow(images[i], cmap=plt.cm.bone)
    
    # label the image with the target value
    p.text(0, 14, str(target[i]))
    p.text(0, 60, str(i))
    
print_faces(faces.images, faces.target, 20)

#Training a Support Vector Machine

from sklearn.svm import SVC

'''The SVC implementation has different important parameters; probably the most
relevant is kernel, which defines the kernel function to be used in our classifier
(think of the kernel functions as different similarity measures between instances).
By default, the SVC class uses the rbf kernel, which allows us to model nonlinear
problems. To start, we will use the simplest kernel, the linear one.'''

svc_1 = SVC(kernel='linear')

'''Before continuing, we will split our dataset into training and testing datasets.'''

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(faces.data, faces.target, test_size=0.25, random_state=0)

'''And we will define a function to evaluate K-fold cross-validation.'''

from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem

def evaluate_cross_validation(clf, X, y, K):
  # create a k-fold croos validation iterator
  cv = KFold(len(y), K, shuffle=True, random_state=0)
  # by default the score used is the one returned by score method of the estimator (accuracy)
  scores = cross_val_score(clf, X, y, cv=cv)
  print scores
  print ("Mean score: {0:.3f} (+/-{1:.3f})").format( np.mean(scores), sem(scores))

evaluate_cross_validation(svc_1, X_train, y_train, 5)

'''Cross-validation with five folds, obtains pretty good results (accuracy of 0.933). In a
few steps we obtained a face classifier.'''

