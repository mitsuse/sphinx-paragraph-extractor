#!/usr/bin/env python3
# coding: utf-8

from setuptools import find_packages
from setuptools import setup

setup(
    name='sphinx-paragraph-extractor',
    version='1.0.4',
    description='A builder for Sphinx to extract paragraphs from docs.',
    url='https://github.com/mitsuse/sphinx-paragraph-extractor',
    author='Tomoya Kose',
    author_email='tomoya@mitsuse.jp',
    install_requires=[
        'sphinx>=2.0.1<3.0.0',
    ],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=[],
    packages=find_packages(exclude=[
        'tests',
    ]),
    entry_points={
        'sphinx.builders': [
            'paragraph-extractor = sphinx_paragraph_extractor',
        ],
    },
)
