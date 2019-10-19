'''
Highlight text based on a specified syntax file with a
corresponding theme file.
'''


import re
import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(
            description='Add syntax coloring to document.')
    parser.add_argument(
            'syntaxfile',
            type=str,
            help='Syntax file binding regex to content.')
    parser.add_argument(
            'themefile',
            type=str,
            help='Theme file binding content to color.')
    parser.add_argument(
            'sourcefile',
            type=str,
            help='File to add proper syntax coloring to.')

    args = parser.parse_args()
    assert os.path.exists(args.syntaxfile), \
        f'There is no syntaxfile at \'{args.syntaxfile}\'.'
    assert os.path.exists(args.themefile), \
        f'There is no themefile at \'{args.themefile}\'.'
    assert os.path.exists(args.sourcefile), \
        f'There is no sourcefile at \'{args.sourcefile}\'.'
    return args


if __name__ == '__main__':
    args = parse_arguments()
    delim = ': '

    priority = {
            'comment': 5,
            'string': 3,
            'string_block': 4
            }

    syntax = {}
    with open(args.syntaxfile, 'r') as infile:
        for line in infile:
            if line[0] == '#':
                continue
            if line[-1] == '\n':
                line = line[:-1]
            regex = eval(delim.join(line.split(delim)[:-1]))
            value = line.split(delim)[-1]
            syntax[regex] = value
    
    theme = {}
    with open(args.themefile, 'r') as infile:
        for line in infile:
            if line[-1] == '\n':
                line = line[:-1]
            value = line.split(delim)[0]
            color = delim.join(line.split(delim)[1:])
            theme[value] = color

    priority = {value: 0 if value not in priority else priority[value] \
        for value in theme}
    priority[None] = -1

    regtheme = {regex: '\033[{}m'.format(theme[syntax[regex]])
                for regex in syntax}
    notheme = '\033[0m'

    colormap = {value: f'\033[{theme[value]}m' for value in theme}
    colormap = {**colormap, None: notheme}

    with open(args.sourcefile, 'r') as infile:
        lines = [l for l in infile]
        line = ''.join(lines)
        
        '''
        is_used = '0'*len(line)
        for regex in regtheme:
            offset = 0
            for match in re.finditer(regex, line, re.MULTILINE):
                g = 0
                if match.groups():
                    g = 1
                # If the regoin has already been matched by some regex.
                print('POSSIBLE MATCH', syntax[regex],regtheme[regex] + line[match.start(g) + offset:match.end(g) + offset] + notheme,'in',line[match.start(0) + offset:match.end(g) + offset])
                if '1' in is_used[match.start(g) + offset:match.end(g) + offset]:
                    continue
                print('MATCH')

                new_line = line[:match.start(g) + offset] \
                    + regtheme[regex] \
                    + line[match.start(g) + offset:match.end(g) + offset] \
                    + notheme \
                    + line[match.end(g) + offset:]
                len_diff = len(new_line) - len(line)
                is_used = is_used[:match.start(g) + offset] \
                    + '1'*(len_diff + match.end(g) - match.start(g)) \
                    + is_used[match.end(g) + offset:]
                offset += len_diff
                line = new_line
        '''

        color = [None]*len(line)
        
        for regex in syntax:
            value = syntax[regex]
            for match in re.finditer(regex, line, re.MULTILINE):
                groups = [0]
                if match.groups():
                    groups = [i + 1 for i,_ in enumerate(match.groups())]
                for g in groups:
                    print('MATCH',value,line[match.start(g):match.end(g)],'in',line[match.start(0):match.end(0)])
                    for i in range(match.start(g),match.end(g)):
                        if priority[value] > priority[color[i]]:
                            color[i] = value
        
        pre_value = None
        offset = 0
        for i,value in enumerate(color):
            if value == pre_value:
                continue
            new_line = line[:i + offset] + colormap[value] + line[i + offset:]
            offset += len(colormap[value])
            line = new_line
            pre_value = value
        print(line)
