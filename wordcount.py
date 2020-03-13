#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Define a helper function to avoid code duplication inside
print_words() and print_top().  Let's call this function create_word_dict.
It should return a Python dictionary data structure with
words as keys, and their counts as values.
"""

import sys

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "???"


def create_word_dict(filename):
    """Returns a word/count dict for this filename."""
    # Your code here
    return


def print_words(filename):
    """Prints one per line '<word> : <count>' sorted by word for the given file."""
    # Your code here
    return


def print_top(filename):
    """Prints the top count listing for the given file."""
    # Your code here
    return


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
