import re
import argparse
import os
from highlighter import mark_syntax, color_line


def parse_arguments():
    parser = argparse.ArgumentParser(
            description='A grep clone implemented using python regex.')
    parser.add_argument(
            'sourcefile',
            type=str,
            help='The file to search for occurences of the regex in.')
    parser.add_argument(
            'regex',
            nargs='+',
            type=str,
            help='The regex to search for in the sourcefile.')
    parser.add_argument(
            '--highlight',
            action='store_true',
            help='Set if turning highlighting on.')
    args = parser.parse_args()
    assert os.path.exists(args.sourcefile), 'There is no sourcefile at \'{args.sourcefile}\'.'
    return args

def not_colored(coloring):
    for c in coloring:
        if c is not None:
            return False
    return True
    
if __name__ == '__main__':
    args = parse_arguments()
    notheme = '\033[0m'
    colors = [f'\033[{i}m' for i in range(31,51)]
    syntax = {regex: i for i,regex in enumerate(args.regex)}
    colormap = {i: colors[i % len(colors)] for i,_ in enumerate(args.regex)}
    colormap = {**colormap, None: notheme}

    print(args)
    
    with open(args.sourcefile) as infile:
        for line in infile:
            line, coloring = mark_syntax(line, syntax)
            if not_colored(coloring):
                continue
            
            if args.highlight:
                line = color_line(line, coloring, colormap)
            print(line,end='')
