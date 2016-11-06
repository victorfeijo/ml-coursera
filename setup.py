# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='Sample',
    long_description=readme,
    author='Victor Feijo',
    author_email='victor.feijoa@gmail.com',
    url='https://github.com/victorfeijo/ml-coursera',
    packages=find_packages(exclude=('tests', 'docs'))
)
