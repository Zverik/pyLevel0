from __future__ import print_function
import readline
from collections import OrderedDict

try:
    input = raw_input
except NameError:
    pass


def separator():
    print('-' * 20)


def read_line(prompt, options=None):
    if options:
        if prompt:
            prompt += ' '
        prompt += '['+options+']'
    prompt += '> '
    try:
        return input(prompt)
    except EOFError:
        print()
        return None


def yes_no(prompt, default=False):
    opts = 'Yn' if default else 'yN'
    while True:
        answer = read_line(prompt, opts)
        if answer is None:
            return default
        answer = answer.strip().lower()
        if answer == '':
            return default
        if answer[0] in ('n', 'f'):
            return False
        if answer[0] in ('y', 't'):
            return True


class Menu(object):
    def __init__(self, title=None):
        self.title = title
        self.items = OrderedDict()

    def add(self, idx, title):
        """Appends a menu item. Index should be specified to make the code self-explanatory."""
        idx = str(idx)
        if len(idx) != 1:
            raise KeyError('Index should be a single character: {}'.format(idx))
        if idx in self.items:
            raise KeyError('Index {} is already set'.format(idx))
        self.items[idx] = title

    def show(self, default=None):
        """Prints a menu and returns a code."""
        if default is not None:
            default = str(default).lower()
        if self.title:
            print(self.title)
            print()
        for k, v in self.items.items():
            print('{}) {}'.format(k, v))
        print()
        while True:
            answer = read_line('Select', default)
            if answer is None:
                return default
            answer = answer.strip().lower()
            if answer == '' and default is not None:
                return default
            if len(answer) == 1 and answer in self.items:
                return answer
