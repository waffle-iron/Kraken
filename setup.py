'''
File: setup.py
Author: Zachary King

Python setup.py file to give meta data and packaging information
for the Kraken project.
'''

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Kraken',
    version='0.1.0',
    description='The Kraken scripting language',
    author='Zachary King',
    author_email='kingzach77@gmail.com'
    packages=['kraken',],
    license='MIT',
    keywords=['kraken', 'language', 'scripting'],
    classifiers=[
        'Programming Language :: Python'
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Languages'
    ]
)
