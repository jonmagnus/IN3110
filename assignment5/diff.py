'''
Strategy:
    Find all matching lines first. It shouldn't be too difficult to match lines in a way that conserves the most amount of matched lines.
'''
import argparse
import os
import numpy as np

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

def print_diff(c, lines_1, lines_2, i, j, outfile):
    '''
    Prints the lines of the file recursively with a sign corresponding to if it was inserted,
    deleted or exists in the longest common subsequence.
    Args:
        c (array): The dp-table corresponding to the longest common subsequences of the substrings.
        lines_1 (list): The list of lines from the first file
        lines_2 (list): The list of lines from the second file
        i (int): The current line we are investigating in the first file
        j (int): The current line we are investigating in the second file
    '''
    # The lines are the same, so we matched them earlier.
    if i > 0 and j > 0 and lines_1[i] == lines_2[j]:
        print_diff(c, lines_1, lines_2, i - 1, j - 1, outfile)
        outfile.write('0 '+ lines_1[i])
    # Iterating on the second file leads us down the optimal path.
    elif j > 0 and (i == 0 or c[i,j - 1] >= c[i - 1][j]):
        print_diff(c, lines_1, lines_2, i, j - 1, outfile)
        outfile.write('- '+ lines_2[j])
    # Iterating on the first file leads us down the optimal path.
    elif i > 0 and (j == 0 or c[i,j - 1] < c[i - 1][j]):
        print_diff(c, lines_1, lines_2, i - 1, j, outfile)
        outfile.write('+ ' + lines_1[i])

if __name__ == '__main__':
    args = parse_arguments()
    with open(args.sourcefile, 'r') as infile:
        lines_1 = [l for l in infile]

    with open(args.otherfile, 'r') as infile:
        lines_2 = [l for l in infile]

    n = len(lines_1)
    m = len(lines_2)

    # Pad files for easier construction of dp-table.
    lines_1 = [0] + lines_1
    lines_2 = [0] + lines_2

    # Solve the longest common subsequence problem.
    '''
    The algorithm uses dynamic programming with table entries c[i,j] corresponding
    to the longest common subsecuence in the substrings A[:i + 1] and B[:j + 1].
    If A[i] matches B[i], we match the entries and add 1 to the length of the longest
    substring in A[:i] and B[:j]. Otherwise we continue to expand the longest substring
    of A[:i] and B[:j + 1] or A[:i + 1] and B[:j].
    '''
    c = np.zeros([n + 1, m + 1])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if lines_1[i] == lines_2[j]:
                c[i,j] = c[i - 1,j - 1] + 1
            else:
                c[i,j] = max(c[i,j - 1], c[i - 1,j])

    outfile = open("diff_output.txt", "w+")

    print_diff(c, lines_1, lines_2, n, m, outfile)

    outfile.close()
