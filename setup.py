#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: X11 Applications :: Qt',
    'Framework :: Twisted',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Natural Language :: English',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(
    name='qt5reactor-fork',
    version='0.2',
    license='MIT',
    classifiers=classifiers,
    author='Tarashish Mishra',
    author_email='sunu@sunu.in',
    description='Twisted Qt Integration',
    long_description=read('README.rst'),
    url='https://github.com/sunu/qt5reactor',
    packages=find_packages(),
    py_modules=['qt5reactor'],
    keywords=['Qt', 'twisted'],
    install_requires=['twisted']
)
