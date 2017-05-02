#!/usr/bin/env python

from distutils.core import setup

setup(name='GitHubUtils',
      version='1.0',
      description='GitHub API Access Utilities',
      author='Caius Brindescu',
      author_email='caius@brindescu.com',
      url='https://github.com/caiusb/github-utils',
      packages=['github'],
      install_requires=['requests']
     )