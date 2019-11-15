'''
Display the predictions of classifier.
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

from data import plot_with_columns
from data import get_split_table, get_labels
from fitting import fit

def visualize_confidence(classifier, table, col1, col2, ax=None, **kwargs):
    '''
    Draw a contour in the prediction area for the classifier given two features to predict on.
    
    :param classifier: Trained classifier to visualize predictions of.
    :param table: The full table to get the range of possible values to predict on.
    :param col1: The first column name.
    :param col2: The second column name.
    :param ax: The canvas to draw on.
    :return: The modified canvas.
    '''
    if ax is None:
        # Generate a new canvas if none was provided.
        ax = plt.subplot(1,1,1)

    x_values = table[col1]
    y_values = table[col2]
    
    x_min = np.min(x_values) - 1
    x_max = np.max(x_values) + 1
    y_min = np.min(y_values) - 1
    y_max = np.max(y_values) + 1

    h = .2
    x = np.arange(x_min, x_max, h)
    y = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(x, y)

    xy_foldout = np.c_[xx.ravel(), yy.ravel()]

    if hasattr(classifier, 'decision_function'):
        Z = classifier.decision_function(xy_foldout)
    else:
        Z = classifier.predict_proba(xy_foldout)[:, 1]

    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, colors=['#ff000080','#0000ff80'], levels=1, **kwargs)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    return ax

def handle_image_generation(classifier, feature_set, imagepath, title=''):
    '''
    Train a classifier and return it's scores on the train and test split.
    Save a contour image of it's predictions if it is only trained on two features.

    :param classifier: A string or object describing a classifier.
    :param feature_set: A list of column names describing the feature set to train the model on.
    :param imagepath: The path to store the contour plot.
    :param title: The title of the plot with scores.
    :return: The train and test scores for the classifier.
    '''
    train_table, test_table = get_split_table()
    train_labels, test_labels = get_labels(train_table, test_table)
    classifier = fit(classifier, feature_set, train_table)
    train_score = classifier.score(train_table[feature_set], train_labels)
    test_score = classifier.score(test_table[feature_set], test_labels)

    if (len(feature_set) == 2):
        fig = plt.figure()
        ax = visualize_confidence(classifier, train_table, *feature_set)
        plot_with_columns(train_table, *feature_set, ax=ax, marker='+', label='train')
        plot_with_columns(test_table, *feature_set, ax=ax, label='test')
        ax.legend()
        try:
            ax.set_title(title.format(train_score=train_score, test_score=test_score))
        except ValueError:
            ax.set_title(title)
        fig.savefig(imagepath)

    return train_score, test_score


if __name__=='__main__':
    from data import get_numerical_columns
    from fitting import classifier_map
    train_table, test_table = get_split_table()
    train_labels, test_labels = get_labels(train_table, test_table)
    feature_options = get_numerical_columns()
    feature_set = np.random.choice(feature_options, size=2)
    fig = plt.figure()
    classifier_name = np.random.choice(list(classifier_map.keys()))
    classifier = fit(classifier_name, feature_set, train_table)
    train_score = classifier.score(train_table[feature_set], train_labels)
    test_score = classifier.score(test_table[feature_set], test_labels)
    ax = visualize_confidence(classifier, train_table, *feature_set)
    plot_with_columns(
            train_table,
            *feature_set,
            ax=ax,
            marker='+',
            label='train',
            )
    plot_with_columns(test_table, *feature_set, ax=ax, label='test')
    ax.set_title(f'{classifier_name}: Test {test_score:.5f} Train {train_score:.5f}')
    ax.legend()
    plt.show()
