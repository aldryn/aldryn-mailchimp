#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_mailchimp import __version__

REQUIREMENTS = [
    'pyrate>=0.5a5'
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='aldryn-mailchimp',
    version=__version__,
    description='Plugins for MailChimp integration.',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-mailchimp',
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
