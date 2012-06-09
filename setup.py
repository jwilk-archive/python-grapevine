'''
*grapevine* (formerly known as *python-pipeline*) lets you create pipelines of
iterators
'''

classifiers = '''
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Topic :: Software Development :: Libraries :: Python Modules
'''.strip().splitlines()

from distutils.core import setup

setup(
    name = 'grapevine',
    version = '1.0',
    license = 'MIT',
    platforms = ['any'],
    description = 'Iterator pipelines',
    long_description = __doc__.strip(),
    classifiers = classifiers,
    url = 'http://jwilk.net/software/python-grapevine',
    author = 'Jakub Wilk',
    author_email = 'jwilk@jwilk.net',
    py_modules = ['grapevine']
)

# vim:ts=4 sw=4 et
