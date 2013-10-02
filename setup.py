#!/usr/bin/env python

from setuptools import setup


long_desc = open('README.md', 'r').read()

setup(
    name="hash-ring-ctypes",
    version='1.0.0',
    description='A fast ctypes-based wrapper around libhashring',
    author='Matt Dennewitz',
    author_email='mattdennwitz@gmail.com',
    long_description=long_desc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
    keywords='hash ring',
    url='https://github.com/mattdennewitz/hash-ring-ctypes/',
    license='BSD',
    packages=['hash_ring'],
    zip_safe=False,
)
