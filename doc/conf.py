import sys
import os

source_suffix = '.txt'
master_doc = 'index'

html_theme = 'haiku'
pygments_style = 'sphinx'

project = u'grapevine'
copyright = u'2007-2012, Jakub Wilk'

def get_version():
    d = {}
    path = os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        'grapevine.py'
    )
    file = open(path)
    try:
        for line in file:
            if line.startswith('__version__ ='):
                exec(line, d)
    finally:
        file.close()
    try:
        return d['__version__']
    except LookupError:
        raise IOError('unexpected end-of-file')

release = version = get_version()

# vim:ts=4 sw=4 et
