#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    import setuptools

    setup = setuptools.setup
except ImportError:
    setuptools = None
    from distutils.core import setup

packages = [
    'speedycloud',
    'speedycloud.object_storage',
]

if sys.version_info < (2, 6):
    error = 'ERROR: speedycloud-python-sdk requires Python Version 2.6 or above.'
    print >> sys.stderr, error
    sys.exit(1)

setup(
    name='speedycloud-python-sdk',
    version='1.0',
    description='SpeedyCloud Object Storage Python SDK',
    long_description='see:\nhttps://github.com/speedycloud/python-sdk\n',
    author='Beijing SpeedyCloud Technology Co., Ltd.',
    author_email='sdk@speedycloud.cn',
    maintainer_email='support@speedycloud.cn',
    license='MIT',
    url='https://github.com/speedycloud/python-sdk',
    platforms='any',
    packages=packages,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['lxml'],
)
