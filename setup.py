#! /usr/bin/env python

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

path_readme = os.path.join(os.path.dirname(__file__), 'README.md')
try:
    import pypandoc
    README = pypandoc.convert(path_readme, 'rst')
except (IOError, ImportError):
    with open(path_readme) as readme:
        README = readme.read()

path_version = os.path.join(os.path.dirname(__file__),
                            'algoliasearchasync/version.py')
with open(path_version, 'r') as f:
    exec(f.read())

setup(
    name='algoliasearchasync',
    version=__version__,
    license='MIT License',
    packages=['algoliasearchasync'],
    packages_data={'algoliasearchasync': ['resources/*.crt']},
    include_package_data=True,
    zip_safe=False,  # Because of the certificate
    install_requires=['algoliasearch>=1.10.1', 'aiohttp>=0.21.6'],
    description='Algolia Search Asyncronous API Client for Python',
    long_description=README,
    author='Algolia Team',
    author_email='support@algolia.com',
    url='https://github.com/algolia/algoliasearch-client-python-async',
    keywords=['algolia', 'pyalgolia', 'search', 'backend', 'hosted', 'cloud',
              'full-text search', 'faceted search', 'async'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Development Status :: 4 - Beta',
    ]
)
