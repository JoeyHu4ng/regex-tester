from parse import parse
import re
import tkinter as tk

# read the test suite file
suite = []
with open('test-suite', 'r') as f:
    for line in f:
        word, status = line.strip().split()
        status = status == 'True'
        suite.append((word, status))


while True:
    regex = parse(input('Enter regex: '))
    print('Regex in python: {0}'.format(regex))
    print('starting the test: ...')
    for case, status in suite:
        x = re.search(regex, case) is not None
        if x != status:
            print('error: case: {0}, expected: {1}\n'.format(case, status))
    print('done!\n')
