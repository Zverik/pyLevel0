#!/usr/bin/env python3
import sys
import os
import console
from . import __version__


def process_arg(arg):
    # TODO
    print('Nope, no argument support yet')


if __name__ == '__main__':
    has_changes = False
    has_data = False
    is_authorized = False

    if len(sys.argv) > 1:
        process_arg(sys.argv[1])

    while True:
        m = console.Menu('cLevel0 {}'.format(__version__))
        m.add('a', 'Add an OSM object')
        if has_data:
            m.add('e', 'Edit data')
            m.add('u', 'Update data from API')
            m.add('s', 'Save data as JOSM XML')
            if has_changes:
                m.add('x', 'Upload data and exit')
        else:
            m.add('e', 'Create data from scratch')
        m.add('q', 'Quit Level0')
        opt = m.show()

        if opt is None or opt == 'q':
            if not has_changes or console.yes_no('You have unsaved changes. Quit?'):
                break