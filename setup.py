
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='ast2json',
      version='0.2.1',
      description='convert a python source code into json-dumpable data (dict and lists with strings, ints, ...)',
      author='Laurent Peuch',
      long_description=long_description,
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/ast2json',
      license='BSD',
      keywords='ast',
      packages=find_packages(),
      install_requires=[],
      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
                   # How mature is this project? Common values are
                   #   3 - Alpha
                   #   4 - Beta
                   #   5 - Production/Stable
                   'Development Status :: 3 - Alpha',

                   # Indicate who your project is intended for
                   'Intended Audience :: Developers',

                   # Pick your license as you wish (should match "license" above)
                   #'License :: OSI Approved :: MIT License',

                   # Specify the Python versions you support here. In particular, ensure
                   # that you indicate whether you support Python 2, Python 3 or both.
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   ],
     )
