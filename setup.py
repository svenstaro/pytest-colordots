#!/usr/bin/env python

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pytest-colordots',
    license='MIT',
    description='Colorizes the progress indicators',
    author='Sven-Hendrik Haase',
    author_email='svenstaro@gmail.com',
    url='https://github.com/svenstaro/pytest-colordots',
    long_description=read("README.md"),
    version='1.0',
    py_modules=['pytest_colordots'],
    entry_points={'pytest11': ['colordots = pytest_colordots']},
    install_requires=['pytest>=2.0', 'colorama'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Testing',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ]
)
