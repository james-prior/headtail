#!/usr/bin/python

'''
Copyright (c) 2016 James Prior

todo
    add options (mostly same as head and tail)
        limit head lines
        limit tail lines
        limit both head and tail lines
        verbose?
        specify files

Copyright (c) 2016 James Prior

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
'''

from __future__ import print_function
import sys
from itertools import islice

n_head_lines = 3
n_tail_lines = 3

def do_file(f):
    f = iter(f)
    for line in islice(f, n_head_lines):
        print(line, end='')

    tail_lines = [None for _ in range(n_tail_lines)]
    n = 0
    for line in f:
        tail_lines[n%n_tail_lines] = line
        n += 1

    if n > n_tail_lines:
        print('...')
    for i in range(n - n_tail_lines, n):
        line = tail_lines[i%n_tail_lines]
        if line is None:
            continue
        print(line, end='')

if __name__ == '__main__':
    do_file(sys.stdin)
