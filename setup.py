'''
python-pipeline lets you create pipelines of iterators.
'''

classifiers = '''\
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules'''.split('\n')

from distutils.core import setup

setup(
	name = 'python-pipeline',
	version = '0.1',
	license = 'GNU GPL 2',
	platforms = ['any'],
	description = 'Iterator pipelines',
	long_description = __doc__.strip(),
	classifiers = classifiers,
	url = 'http://python-pipeline.googlecode.com/',
	author = 'Jakub Wilk',
	author_email = 'ubanus@users.sf.net',
	py_modules = ['pipeline']
)

# vim:ts=4 sw=4 noet
