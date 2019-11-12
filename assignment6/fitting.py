from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB

from data import get_table, get_numerical_columns


def fit(classifier, feature_set, train_table):
    ''' Train a classifier on the specified feature set.
    '''
    train_labels = train_table[['diabetes']]
    train_labels['diabetes'] = train_labels['diabetes'].apply(lambda val: 1 if val == 'pos' else 0)#.values.reshape(-1,1)
    print(train_labels)
    classifier.fit(train_table[feature_set], train_labels)
    score = classifier.score(train_labels, train_labels)
    print(score)
    
if __name__=='__main__':
    table = get_table()
    print(table)

    train_table, test_table = train_test_split(table, test_size=.2)
    
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

    train_table, test_table = train_test_split(table, test_size=.2)
    feature_set = get_numerical_columns(table)
    fit(classifiers[0], feature_set, train_table)
