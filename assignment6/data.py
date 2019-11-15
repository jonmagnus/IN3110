'''
Retrieve and filter data for classification of diabetes.
'''


import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split

def get_table():
    '''
    Return the diabetes table as a pandas dataframe.
    
    :return: A pandas dataframe generated from the csv table.
    '''
    filename = 'diabetes.csv'
    filedir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(filedir, filename)
    assert os.path.exists(filepath), f'Missing diabetes.csv at \'{filepath}\''
    table = pd.read_csv(filepath, index_col=0)
    # Filter out rows containing nan
    table.dropna(inplace=True)
    return table

def get_split_table(test_size=.2):
    '''
    Return the diabetes table split into train and test partitions.

    :param test_size: The fraction of the total table allocated for testing.
    :return: A train and test table as a partition of the diabetes table.
    '''
    table = get_table()
    train_table, test_table = train_test_split(table, test_size=test_size)
    return train_table, test_table

def get_labels(*args):
    '''
    Filter of the diabetes label for any number of valid pandas dataframes.

    :param args: A list of pandas dataframes.
    :return: A list of labels corresponding to the tables provided.
    '''
    label_list = []
    for table in args:
        labels = table[['diabetes']].copy()
        labels['diabetes'] = labels['diabetes'].apply(lambda val: 1 if val == 'pos' else 0)
        label_list.append(labels)
    return label_list
        

def get_numerical_columns(table=None):
    ''' 
    Return all column names of the provided table except the diabetes column.
    The diabetes column is not number valued and cannot be used for classification.

    :param table: The table to retrieve the column names from.
    :return: The column names of the table except 'diabetes'.
    '''

    if table is None:
        table = get_table()

    columns = table.drop(['diabetes'], axis=1).columns
    return columns

def plot_with_columns(table, col1, col2, **kwargs):
    '''
    Generate a scatter plot from two columns of a table.
    
    :param table: The dataframe to retrieve the columns from.
    :param col1: The first column name. Is displayed along the x-axis.
    :parma col2: The second column name. Is displayed along the y-axis.
    '''
    c1 = kwargs.get('c1', 'b')
    c2 = kwargs.get('c2', 'r')
    
    colors = table['diabetes'].apply(lambda val: c1 if val == 'pos' else c2)
    kwargs_filter = ['marker', 'vmin', 'vmax', 'label', 'ax']
    f_kwargs = {key: kwargs.get(key) for key in kwargs_filter if key in kwargs}
    return table.plot.scatter(x=col1, y=col2, c=colors, **f_kwargs)

def plot_all_matches(table, columns, **kwargs):
    '''
    Generate a grid of plots similar to a correlation matrix.

    :param table: The dataframe to retrieve the columns from.
    :param columns: A subset of the table's columns to display the correlation between.
    '''
    n = len(columns)
    fig, axes = plt.subplots(n, n)
    for i,col1 in enumerate(columns):
        for j,col2 in enumerate(columns):
            plot_with_columns(table, col1, col2, ax=axes[i][j], **kwargs)
            plt.xlabel(col1)
            plt.ylabel(col2)

    return fig, axes

if __name__=='__main__':
    import numpy as np
    table = get_table()
    columns = get_numerical_columns(table)
    plot_all_matches(table, np.random.choice(columns, size=4))
    plt.show()
