#!/usr/bin/python3

from setuptools import find_packages, setup

packages = ['comrade.' + x for x in find_packages('comrade')]
setup(
    name='elasticsearch-comrade',
    version='1.1.3',
    description='Elasticsearch admin panel built for ops and monitoring',
    author='Moshe Zada',
    author_email='',
    packages=['comrade'] + packages,
    include_package_data=True,
    install_requires=[
        'sanic',
        'ujson',
        'elasticsearch-async',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'comrade = comrade.index:main',
        ]
    }
)
