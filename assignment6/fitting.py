from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB

from data import get_split_table, get_numerical_columns

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
    ''' Train a classifier on the specified feature set.
    '''
    if isinstance(classifier, str):
        if classifier not in classifier_map.keys():
            raise ValueError(f'No classifier with name \'{classifier}\'')
        classifier = classifier_map[classifier]

    train_data = train_table[feature_set].copy()
    train_labels = train_table[['diabetes']].copy()
    train_labels['diabetes'] = train_labels['diabetes'].apply(lambda val: 1 if val == 'pos' else 0)
    classifier.fit(train_data, train_labels)
    score = classifier.score(train_data, train_labels)
    print(f'Training score {score}')
    return classifier
    
if __name__=='__main__':
    # Classifier list retrieved from 
    # https://scikit-learn.org/0.15/auto_examples/plot_classifier_comparison.html
    classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="linear", C=0.025),
        SVC(gamma=2, C=1),
        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        AdaBoostClassifier(),
        GaussianNB()]

    train_table, test_table = get_split_table()
    feature_set = get_numerical_columns(train_table)
    fit(classifiers[0], feature_set, train_table)
