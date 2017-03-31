import io
import os

extensions = [
    'sphinx.ext.doctest',
]

source_suffix = '.rst'
master_doc = 'index'

html_theme = 'haiku'
pygments_style = 'sphinx'

project = 'grapevine'
copyright = '2007-2015, Jakub Wilk'

def get_version():
    path = os.path.join(
        os.path.dirname(__file__),
        '../changelog'
    )
    with io.open(path, encoding='UTF-8') as file:
        line = file.readline()
    return line.split()[1].strip('()')

release = version = get_version()

# vim:ts=4 sts=4 sw=4 et
