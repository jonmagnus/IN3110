import re
import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(
            description='Add syntax coloring to document.')
    parser.add_argument('syntaxfile', type=str, help='Syntax file binding regex to content.')
    parser.add_argument('themefile', type=str, help='Theme file binding content to color.')
    parser.add_argument('sourcefile', type=str, help='File to add proper syntax coloring to.')

    args = parser.parse_args()
    assert os.path.exists(args.syntaxfile), f'There is no syntaxfile at \'{args.syntaxfile}\'.'
    assert os.path.exists(args.themefile), f'There is no themefile at \'{args.themefile}\'.'
    assert os.path.exists(args.sourcefile), f'There is no sourcefile at \'{args.sourcefile}\'.'
    return args

if __name__ == '__main__':
    args = parse_arguments()
    
    delim = ': '
    
    syntax = {}
    with open(args.syntaxfile, 'r') as infile:
        for line in infile:
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
    
    print('syntax', syntax)
    print('theme', theme)

    regtheme = {regex: '\033[{}m'.format(theme[syntax[regex]]) for regex in syntax}
    notheme = '\033[0m'
    
    with open(args.sourcefile, 'r') as infile:
        lines = [l for l in infile]
        line = ''.join(lines)
        '''
        offset = 0
        while offset < len(line):
            #print('line',line)
            for regex in regtheme:
                print('regex',regex)
                match = re.match(regex,line[offset:])
                if match:
                    print('MATCH', match.group(0), match.groups(),syntax[regex])
                    g = 0
                    if match.groups():
                        g = 1
                    new_line = line[:offset + match.start(g)] \
                           + regtheme[regex] \
                           + line[offset:offset + match.end(g)] \
                           + notheme \
                           + line[offset + match.end(g):]
                    #print('newline',new_line)

                    try:
                        offset += len(new_line) - len(line) + len(match.group(g)) - 1
                    except Exception as e:
                        print(f'new_line \'{new_line}\'\nline \'{line}\'\ngroup \'{match.group(g)}\'')
                        print(f'match.groups() \'{match.groups()}\'')
                        raise e
                    line = new_line
                    break
            #print('offset',offset)
            offset += 1
        '''

        is_used = [0]*len(line)
        for regex in regtheme:
            offset = 0
            for match in re.finditer(regex,line):
                g = 0
                if match.groups():
                    g = 1
                if 1 in is_used[match.start(g):match.end(g)]:
                    continue

                new_line = line[:match.start(g) + offset] \
                           + regtheme[regex] \
                           + line[match.start(g) + offset:match.end(g) + offset] \
                           + notheme \
                           + line[match.end(g) + offset:]
                len_diff = len(new_line) - len(line)
                is_used = is_used[:match.start(g) + offset] \
                          + [1]*len_diff \
                          + is_used[match.end(g) + offset:]
                offset += len_diff
                line = new_line

        print(line)
