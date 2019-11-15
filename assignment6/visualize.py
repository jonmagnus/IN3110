import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

from data import plot_with_columns
from data import get_split_table, get_labels
from fitting import fit

def visualize_confidence(classifier, table, col1, col2, ax=None, **kwargs):
    if ax is None:
        ax = plt.subplot(1,1,1)

    x_values = table[col1]
    y_values = table[col2]
    
    x_min = np.min(x_values) - .5
    x_max = np.max(x_values) + .5
    y_min = np.min(y_values) - .5
    y_max = np.max(y_values) + .5

    h = .2
    x = np.arange(x_min, x_max, h)
    y = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(x, y)

    print('xx, yy', xx.shape, yy.shape)
    print('ravel', xx.ravel().shape, yy.ravel().shape)
    
    xy_foldout = np.c_[xx.ravel(), yy.ravel()]
    print('xy_foldout', xy_foldout.shape)
    if hasattr(classifier, 'decision_function'):
        Z = classifier.decision_function(xy_foldout)
    else:
        Z = classifier.predict_proba(xy_foldout)[:, 1]

    c_red = (.5,0,0)
    c_blue = (0,0,.5)
    c_red = 'r'
    c_blue = 'b'
    colormap = np.array([c_red if x > 0 else c_blue for x in Z])

    Z = Z.reshape(xx.shape)
    colormap = colormap.reshape((*xx.shape,))
    print('Z', Z.shape)
    print('colormap',colormap.shape)
    ax.contourf(xx, yy, Z, colors=['#ff000080','#0000ff80'], levels=1, **kwargs)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    return ax

def handle_image_generation(
        classifier,
        feature_set=['pregnant', 'glucose'], 
        imagepath=os.path.join(os.getcwd(), 'resources', 'image.svg'),
        title='',
        ):
    train_table, test_table = get_split_table()
    train_labels, test_labels = get_labels(train_table, test_table)
    classifier = fit(classifier, feature_set, train_table)
    train_score = classifier.score(train_table[feature_set], train_labels)
    test_score = classifier.score(test_table[feature_set], test_labels)

    if (len(feature_set) == 2):
        fig = plt.figure()
        ax = visualize_confidence(classifier, train_table, *feature_set)
        plot_with_columns(train_table, *feature_set, ax=ax, marker='+')
        plot_with_columns(test_table, *feature_set, ax=ax)
        try:
            ax.set_title(title.format(train_score=train_score, test_score=test_score))
        except ValueError:
            ax.set_title(title)
        fig.savefig(imagepath)

    return train_score, test_score


if __name__=='__main__':
    train_table, test_table = get_split_table()
    train_labels, test_labels = get_labels(train_table, test_table)
    feature_set = ['pregnant', 'glucose']
    fig = plt.figure()
    from fitting import classifier_map
    print('classifier keys', classifier_map.keys())
    classifier = np.random.choice(list(classifier_map.keys()))
    print('classifier', classifier)
    classifier = fit(classifier, feature_set, train_table)
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
    ax.set_title(f'SCORES: Test {test_score:.5f} Train {train_score:.5f}')
    ax.legend()
    plt.show()
