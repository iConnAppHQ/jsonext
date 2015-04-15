#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='iconn_jsonext',
    version='1.0',
    description='Well-structured helpers to help serializing commonly '
                'encountered structures to JSON (like datetime, asdict(), '
                ' etc.',
    long_description=read('README.rst'),
    author='Mike Klimin',
    author_email='mike@iconnapp.ru',
    url='http://github.com/iConnAppHQ/jsonext',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['simplejson',
                      'times',
                      'pymongo'],
)
