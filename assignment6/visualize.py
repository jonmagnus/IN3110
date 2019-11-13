import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from data import plot_with_columns

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

    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap='RdBu', **kwargs)
    plot_with_columns(table, col1, col2, ax=ax, **kwargs)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    return ax

if __name__=='__main__':
    from data import get_split_table, get_labels
    from fitting import fit
    train_table, test_table = get_split_table()
    train_labels, test_labels = get_labels(train_table, test_table)
    feature_set = ['pregnant', 'glucose']
    classifier = fit('svc', feature_set, train_table)
    visualize_confidence(classifier, train_table, *feature_set)
    print(f'Test score {classifier.score(test_table[feature_set], test_labels)}')
    plt.show()
