'''
*python-pipeline* lets you create pipelines of iterators.
'''

classifiers = '''\
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Software Development :: Libraries :: Python Modules'''.split('\n')

from distutils.core import setup
import os

os.putenv('TAR_OPTIONS', '--owner root --group root --mode a+rX')

setup(
	name = 'python-pipeline',
	version = '0.1.3+py3k',
	license = 'MIT',
	platforms = ['any'],
	description = 'Iterator pipelines',
	long_description = __doc__.strip(),
	classifiers = classifiers,
	url = 'http://python-pipeline.googlecode.com/',
	author = 'Jakub Wilk',
	author_email = 'jwilk@jwilk.net',
	py_modules = ['pipeline']
)

# vim:ts=4 sw=4 noet
