from setuptools import setup, find_packages

install_requires = []

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: BSD License
License :: OSI Approved :: GNU General Public License (GPL)
Programming Language :: Python
Development Status :: 3 - Alpha
"""

setup(
    name = 'dplapy',
    version = '0.1',  # remember to update dplapy/__init__.py on release!
    url = 'http://github.com/anarchivist/dplapy',
    author = 'Jay Luker',
    author_email = 'lbjay@reallywow.com'
    license = 'GPL/BSD',
    packages = find_packages(),
    install_requires = install_requires,
    description = 'Interact with the DPLA API',
    classifiers = filter(None, classifiers.split('\n')),
)
