'''Naïve Bayes is a simple but powerful classifier based on a probabilistic model
derived from the Bayes' theorem. Basically it determines the probability that an
instance belongs to a class based on each of the feature value probabilities. The naïve
term comes from the fact that it assumes that each feature is independent of the rest,
that is, the value of a feature has no relation to the value of another feature.'''

'''Despite being very simple, it has been used in many domains with very good
results. The independence assumption, although a naïve and strong simplification,
is one of the features that make the model useful in practical applications. Training
the model is reduced to the calculation of the involved conditional probabilities,
which can be estimated by counting frequencies of correlations between feature
values and class values.
One of the most successful applications of Naïve Bayes has been within the field
of Natural Language Processing (NLP). NLP is a field that has been much related
to machine learning, since many of its problems can be formulated as a classification
task. Usually, NLP problems have important amounts of tagged data in the form
of text documents. This data can be used as a training dataset for machine
learning algorithms.'''

'''As usual, we first start by importing our pylab environment:'''

%pylab inline

'''Our dataset can be obtained by importing the fetch_20newgroups function from the
sklearn.datasets module. We have to specify if we want to import a part or all of
the set of instances (we will import all of them).'''

from sklearn.datasets import fetch_20newsgroups
news = fetch_20newsgroups(subset='all')
