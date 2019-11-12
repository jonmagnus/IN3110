import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split

def get_table():
    filename = 'diabetes.csv'
    filedir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(filedir, filename)
    assert os.path.exists(filepath), f'Missing diabetes.csv at \'{filepath}\''
    table = pd.read_csv(filepath, index_col=0)
    # Filter out rows containing nan
    table.dropna(inplace=True)
    return table

def get_split_table(test_size=.2):
    table = get_table()
    train_table, test_table = train_test_split(table, test_size=test_size)
    return train_table, test_table

def get_numerical_columns(table):
    columns = table.drop(['diabetes'], axis=1).columns
    return columns

def plot_with_columns(table, col1, col2, **kwargs):
    ''' Generate a scatter plot from two columns of a table.
    '''
    for col in [col1, col2]:
        assert type
    colors = table['diabetes'].apply(lambda val: 'b' if val == 'pos' else 'r')
    return table.plot.scatter(x=col1, y=col2, c=colors, **kwargs)

def plot_all_matches(table, columns, **kwargs):
    ''' Generate a grid of plots similar to a correlation matrix.
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
    table = get_table()
    print(table)
    columns = table.drop(['diabetes'], axis=1).columns
    plot_all_matches(table, columns[:4])
    plt.show()
