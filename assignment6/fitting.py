'''
Train and fit classification models.
'''

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB

# List of available classifiers, with strings mapping to the appropriate object.
# Classifier list retrieved from 
# https://scikit-learn.org/0.15/auto_examples/plot_classifier_comparison.html
classifier_map = {
        'kneighbor': KNeighborsClassifier(3),
        'linear_svc': SVC(kernel="linear", C=0.025),
        'svc': SVC(gamma=2, C=1),
        'decision_tree': DecisionTreeClassifier(max_depth=5),
        'random_forest': RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        'adaboost': AdaBoostClassifier(),
        'gassuiannb': GaussianNB()
        }

def fit(classifier, feature_set, train_table):
    '''
    Train a classifier on the specified feature set.
    
    :param classifier: String or object describing a classifier.
    :param feature_set: The column names of the following table used for prediction.
    :param train_table: The dataframe used for training the model.
    :return: The trained classifier.
    '''
    if isinstance(classifier, str):
        if classifier not in classifier_map.keys():
            raise ValueError(f'No classifier with name \'{classifier}\'')
        classifier = classifier_map[classifier]

    train_data = train_table[feature_set].copy()
    train_labels = train_table[['diabetes']].copy()
    train_labels['diabetes'] = train_labels['diabetes'].apply(lambda val: 1 if val == 'pos' else 0)
    classifier.fit(train_data, train_labels)
    return classifier
    
if __name__=='__main__':
    from data import get_split_table, get_numerical_columns, get_labels
    train_table, test_table = get_split_table()
    train_labels, test_labels = get_labels(train_table, test_table)
    feature_set = get_numerical_columns(train_table)
    import random
    classifier = fit(random.choice(list(classifier_map.keys())), feature_set, train_table)
    train_score = classifier.score(train_table[feature_set], train_labels)
    test_score = classifier.score(test_table[feature_set], test_labels)
    print(f'train_score {train_score} test_score {test_score}')
