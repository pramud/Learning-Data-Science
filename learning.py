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

