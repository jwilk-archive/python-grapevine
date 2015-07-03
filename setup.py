# encoding=UTF-8

# Copyright © 2008-2015 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
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
    return d['__version__']

cmdclass = {}

if sphinx_setup_command is not None:
    cmdclass['build_doc'] = sphinx_setup_command.BuildDoc

distutils.core.setup(
    name='grapevine',
    version=get_version(),
    license='MIT',
    platforms=['any'],
    description='iterator pipelines',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='http://jwilk.net/software/python-grapevine',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    py_modules=['grapevine'],
    cmdclass=cmdclass,
)

# vim:ts=4 sts=4 sw=4 et
