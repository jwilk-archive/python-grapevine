'''
*grapevine* (formerly known as *python-pipeline*) lets you create pipelines of
iterators.
'''

import distutils.core
try:
    import sphinx.setup_command as sphinx_setup_command
except ImportError:
    sphinx_setup_command = None

classifiers = '''
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Topic :: Software Development :: Libraries :: Python Modules
'''.strip().splitlines()

def get_version():
    d = {}
    file = open('grapevine.py')
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

cmdclass = {}

if sphinx_setup_command is not None:
    cmdclass['build_doc'] = sphinx_setup_command.BuildDoc

distutils.core.setup(
    name = 'grapevine',
    version = get_version(),
    license = 'MIT',
    platforms = ['any'],
    description = 'iterator pipelines',
    long_description = __doc__.strip(),
    classifiers = classifiers,
    url = 'http://jwilk.net/software/python-grapevine',
    author = 'Jakub Wilk',
    author_email = 'jwilk@jwilk.net',
    py_modules = ['grapevine'],
    cmdclass = cmdclass,
)

# vim:ts=4 sw=4 et
