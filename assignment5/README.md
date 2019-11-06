# Assignment 5

Assignment 5 consist of a syntax highlighting script, with highlighting opportunities for python, C and diff. It also have an implementation of grep and diff.

# Usage

```bash

python3 highlighter.py python.syntax python.theme demo.py
# Highlights demo.py

python3 highlighter.py c.syntax c.theme demo.c
# Highlights demo.c

python3 grep.py demo.py "in" "for" --highlight
# Prints all lines with in and for in demo.py with the words
# in color.

python3 diff.py diff_demo1.txt diff_demo2.txt
#Writes difference to file, diff_output.txt, with unmodified lines marked as 0, added lines marked as +, and deleted lines as -.   

python3 highlighter.py diff.syntax diff.theme diff_output.txt
# Marks added lines with green and deleted lines in red.
```

# Installation

To use the diff you need numpy

```bash
pip3 install numpy
```

# Python highlighter

The python highlighter has syntax highlighting for:
- comments
- import-statements
- special forms
- try-excepts
- if-statements
- function definitions
- functions
- classes
- strings
- for-loops
- while-loops
- variable declarations


# C highlighter

The C highlighter has syntax highlighting for:

- comments
- compiler
- type
- function
- string
- char
- libraries
- return
- struct
