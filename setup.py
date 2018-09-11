#!/usr/bin/env python
import os
from setuptools import setup, find_packages

import versioneer


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
    name='qt5reactor',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='MIT',
    classifiers=classifiers,
    author='Christopher R. Wood',
    author_email='chris@leastauthority.com',
    description='Twisted Qt Integration',
    long_description=read('README.rst'),
    url='https://github.com/sunu/qt5reactor',
    packages=find_packages("src"),
    package_dir={"": "src"},
    keywords=['Qt', 'twisted'],
    install_requires=['pyqt5', 'twisted'],
    extras_require={
        "test": [
            "coverage",
            "pytest",
            "pytest-cov",
            "pytest-twisted",
            "tox>=3.1",
        ],
    },
)
