#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
#history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='LEMON: Local Expansion via Minimum One Norm',
    version='1.0.1',
    description='',
    long_description=readme + '\n\n' + history,
    author='Yixuan Li',
    author_email='yl2363@cornell.edu',
    url='https://github.com/YixuanLi/LEMON',
    packages=[
        'LEMON',
    ],
    entry_points={'console_scripts': ['LEMON = LEMON.__main__:main']},
    package_dir={'LEMON':
                 'LEMON'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv2",
    zip_safe=False,
    keywords='LEMON',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    #test_suite='tests',
    #tests_require=test_requirements
)
