'''The number of parameters (and consequently, the amount of training
data needed to adequately estimate them) would rapidly grow if we add more
features or higher order terms. This phenomenon, present in every machine learning
method, is called the idem curse of dimensionality: when the number of parameters
of a model grows, the data needed to learn them grows exponentially'''

'''This notion is closely related to the problem of overfitting mentioned earlier. As our
training data is not enough, we risk producing a model that could be very good at
predicting the target class on the training dataset but fail miserably when faced with
new data, that is, our model does not have the generalization power. That is why it is
so important to evaluate our methods on previously unseen data'''

'''The general rule is that, in order to avoid overfitting, we should prefer simple (that
is, with less parameters) methods, something that could be seen as an instantiation
of the philosophical principle of Occam's razor, which states that among competing
hypotheses, the hypothesis with the fewest assumptions should be selected.
However, we should also take into account Einstein's words:
"Everything should be made as simple as possible, but not simpler."'''

'''The idem curse of dimensionality may suggest that we keep our models simple,
but on the other hand, if our model is too simple we run the risk of suffering
from underfitting. Underfitting problems arise when our model has such a low
representation power that it cannot model the data even if we had all the training
data we want. We clearly have underfitting when our algorithm cannot achieve good
performance measures even when measuring on the training set.'''

'''As a result, we will have to achieve a balance between overfitting and underfitting.
This is one of the most important problems that we will have to address when
designing our machine learning models.'''

'''SVM has become one of the state-of-the-art machine learning models for many tasks
with excellent results in many practical applications. One of the greatest advantages
of SVM is that they are very effective when working on high-dimensional spaces,
that is, on problems which have a lot of features to learn from. They are also very
effective when the data is sparse (think about a high-dimensional space with very
few instances). Besides, they are very efficient in terms of memory storage, since only
a subset of the points in the learning space is used to represent the decision surfaces.'''

'''To mention some disadvantages, SVM models could be very calculation intensive
while training the model and they do not return a numerical indicator of how
confident they are about a prediction. However, we can use some techniques such as
K-fold cross-validation to avoid this, at the cost of increasing the computational cost.'''


'''SVM IN R E

We will focus on the last block of R code that generates the metric multidimensional scaling (MDS) of the distances separating the 150 flowers calculated from sepal and petal length and width (i.e., the dist function applied to the first four columns of the iris data). Species plays no role in the MDS with the flowers positioned in a two-dimensional space in order to reproduce the pairwise Euclidean distances. However, species is projected onto the plot using color, and the observations acting as support vectors are indicated with plus signs (+).

The setosa flowers are represented by black circles and black plus signs. These points are separated along the first dimension from the versicolor species in red and virginica in green. The second dimension, on the other hand, seems to reflect some within-species sources of differences that do not differentiate among the three iris types.

We should recall that the dist function calculates pairwise distances in the original space without any kernel transformation. The support vectors, on the other hand, were identified from the svm function using a radial kernel and then projected back onto the original observation space. Of course, we can change the kernel, which defaults to “radial” as in this example from the R package. A linear kernel may do just as well with the iris data, as you can see by adding kernel=”linear” to the svm function in the above code.


It appears that we do not need all 150 flowers in order to identify the iris species. We know this because the svm function correctly classifies over 97% of the flowers with 51 support vectors (also called “landmarks” as noted in my last post Seeing Similarity in More Intricate Dimensions). The majority of the +’s are located between the two species with the greatest overlap. I have included the pictures so that the similarity of the red and green categories is obvious. This is where there will be confusion, and this is where the only misclassifications occur. If your iris is a setosa, your identification task is relatively easy and over quickly. But suppose that your iris resembles those in the cluster of red and green pluses between versicolor and virginica. This is where the finer distinctions are being made.

By design, this analysis was kept brief to draw an analogy between support vector machines and finder guides that we have all used to identify unknown plants and animals in the wild. Hopefully, it was a useful comparison that will help you understand how we classify new observations by measuring their distances in a kernel metric from a more limited set of support vectors (a type of global positioning with a minimal number of landmarks or exemplars as satellites).

When you are ready with your own data, you can view the videos from Chapter 9 of An Introduction to Statistical Learning with Applications in R to get a more complete outline of all the steps involved. My intent was simply to disrupt the feature mindset that relies on the cumulative contributions of separate attributes (e.g., the relative impact of each independent variable in a prediction equation). As objects become more complex, we stop seeing individual aspects and begin to bundle features into types or categories. We immediately recognize the object by its feature configuration, and these exemplars or landmarks become the new basis for our support vector representation.

'''
