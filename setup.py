#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='ast2json',
      version='0.2',
      description='convert a python source code into json-dumpable data (dict and lists with strings, ints, ...)',
      author='Laurent Peuch',
      long_description=open('README.rst', 'r').read(),
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/ast2json',
      py_modules=['ast2json'],
      license='BSD',
      keywords='ast',
     )
