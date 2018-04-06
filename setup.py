#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup
import sys

if sys.argv[-1] == 'publish':
    print("Remember to update the Changelog's version and date in README.rst and stage the changes")
    input("Press Enter to continue...")
    os.system("bumpversion --allow-dirty minor")
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to update the repo now:")
    print("  git push origin master")
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='boxme-users',
    version='0.1',
    description="""Custom user model for Django >= 1.5 with the same behaviour as Django's default User but with email instead of username.""",
    long_description=readme,
    author='DiepDT',
    author_email='diepdt@peacesoft.net',
    url='https://github.com/vituocgia/boxme-users',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        "Django >= 1.5",
    ],
    license='BSD License',
    zip_safe=False,
    keywords='django custom user auth model email without username',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
