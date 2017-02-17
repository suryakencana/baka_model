"""
 # Copyright (c) 2017 Boolein Integer Indonesia, PT.
 # suryakencana 2/17/17 @author nanang.suryadi@boolein.id
 #
 # You are hereby granted a non-exclusive, worldwide, royalty-free license to
 # use, copy, modify, and distribute this software in source code or binary
 # form for use in connection with the web services and APIs provided by
 # Boolein.
 #
 # As with any software that integrates with the Boolein platform, your use
 # of this software is subject to the Boolein Developer Principles and
 # Policies [http://developers.Boolein.com/policy/]. This copyright notice
 # shall be included in all copies or substantial portions of the software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 # THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 # FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 # DEALINGS IN THE SOFTWARE
 # 
 # setup.py
"""

# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import re
from codecs import open
from setuptools import find_packages
from setuptools import setup
from setuptools.command.test import test as _test

###############################################################################

NAME = 'baka model'
DESC = 'Baka: Skeleton framework built top of pyramid'
AUTHOR = 'Nanang Suryadi'
AUTHOR_EMAIL = 'nanang.ask@gmail.com'
URL = ''
LICENSE = 'Simplified (2-Clause) BSD License'
KEYWORDS = ['model', 'sqlalchemy', 'framework']
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Environment :: Web Environment',
    'Framework :: Pyramid',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
]
INSTALL_REQUIRES = [
    'setuptools',
    'pyramid',
    'sqlalchemy',
    'zope.sqlalchemy',
    'psycopg2',
    'python-dateutil',
    'transaction',
    'pyramid_tm',
    'sqlalchemy_utils',
    'awesome-slugify',
    'python-dateutil',
    'bcrypt',
]
EXTRAS_REQUIRE = {}
ENTRY_POINTS = {}

with open('README.md', encoding='utf-8') as fp:
    LONGDESC = fp.read()

###############################################################################

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION_FILE = os.path.join(HERE, 'baka_model', '__init__.py')


def get_version():
    """Extract package __version__"""
    with open(VERSION_FILE, encoding='utf-8') as fp:
        content = fp.read()
    match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Could not extract package __version__")


class test(_test):
    def run(self):
        print('please run tox instead')


if __name__ == "__main__":
    setup(name=NAME,
          version=get_version(),
          description=DESC,
          long_description=LONGDESC,
          classifiers=CLASSIFIERS,
          keywords=KEYWORDS,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          url=URL,
          license=LICENSE,
          install_requires=INSTALL_REQUIRES,
          extras_require=EXTRAS_REQUIRE,
          entry_points=ENTRY_POINTS,
          cmdclass={'test': test},
          packages=find_packages(include=['baka_model', 'baka_model.*']),
          zip_safe=False)
