import re
import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(
            description='A grep clone implemented using python regex.')
    parser.add_argument(
            'sourcefile',
            type=str,
            help='The file to search for occurences of the regex in.')
    parser.add_argument(
            'regex',
            type=str,
            help='The regex to search for in the sourcefile.')
    parser.add_argument(
            '--highlight',
            action='store_true',
            help='Set if turning highlighting on.')
    args = parser.parse_args()
    assert os.path.exists(args.sourcefile), 'There is no sourcefile at \'{args.sourcefile}\'.'
    return args
    
if __name__ == '__main__':
    args = parse_arguments()
    notheme = '\033[0m'
    color = '\033[31m'

    with open(args.sourcefile) as infile:
        for line in infile:
            match = re.search(args.regex,line)
            if match:
                if args.highlight:
                    line = line[:match.start(0)] \
                           + color \
                           + line[match.start(0):match.end(0)] \
                           + notheme \
                           + line[match.end(0):]
                print(line)
