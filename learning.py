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
