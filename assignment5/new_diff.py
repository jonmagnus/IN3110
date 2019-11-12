'''
Strategy:
    Find all matching lines first. It shouldn't be too difficult to match lines in a way that conserves the most amount of matched lines.
'''
import argparse as argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(
            description='A diff clone implemented in python.')
    parser.add_argument(
            'sourcefile',
            type=str,
            help='The first file to compare.')
    parser.add_argument(
            'otherfile',
            type=str,
            help='The second file to compare.')
    args = parser.parse_args()
    assert os.path.exists(args.sourcefile), 'There is no sourcefile at \'{args.sourcefile}\'.'
    assert os.path.exists(args.otherfile), 'There is no otherfile at \'{args.otherfile}\'.'
    return args

def print_diff(c, lines_1, lines_2, i, j):
    if i >= 0 and j >= 0 and lines_1[i] == lines_2[j]:
        print_diff(c, lines_1, lines_2, i - 1, j - 1)
        print('0', lines_1[i], end='')
    elif j >= 0 and (i == -1 or c[i][j - 1] >= c[i - 1][j]):
        print_diff(c, lines_1, lines_2, i, j - 1)
        print('+', lines_2[j], end='')
    elif i >= 0 and (j == -1 or c[i][j - 1] < c[i - 1][j]):
        print_diff(c, lines_1, lines_2, i - 1, j)
        print('-', lines_1[i], end='')

if __name__ == '__main__':
    args = parse_arguments()
    with open(args.sourcefile, 'r') as infile:
        lines_1 = [l for l in infile]

    with open(args.otherfile, 'r') as infile:
        lines_2 = [l for l in infile]

    n = len(lines_1)
    m = len(lines_2)

    # Solve the longest common subsequence problem.
    c = [[0]*m]*n
    for i in range(n):
        for j in range(m):
            if lines_1[i] == lines_2[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    
    print_diff(c, lines_1, lines_2, n - 1, m - 1)
