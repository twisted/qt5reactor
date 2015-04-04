#!/usr/bin/env python
import os
from setuptools import setup, find_packages
from glob import glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

classifiers = [
    'Development Status :: 1 - Planning',
    'Environment :: X11 Applications :: Qt',
    'Framework :: Twisted',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Natural Language :: English',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(
    name='qt5reactor-fork',
    version='0.1',
    license='MIT',
    classifiers=classifiers,
    author='Tarashish Mishra',
    author_email='sunu@sunu.in',
    description='Twisted Qt Integration',
    long_description=read('README.rst'),
    url='https://github.com/sunu/qt5reactor',
    #download_url='https://github.com/ghtdak/qtreactor/tarball/master/#egg-qt4reactor.1.6',
    #scripts=glob("./bin/*"),
    packages=find_packages(),
    py_modules=['qt5reactor'],
    keywords=['Qt', 'twisted'],
    install_requires=['twisted']
)
