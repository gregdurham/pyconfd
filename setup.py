# -*- coding: utf-8 -*-

import re
from setuptools import setup

requires = [
    'Jinja2==2.7.3',
    'PyYAML==3.11',
    'docopt==0.6.1',
    'pykwalify==14.08',
    'python-etcd==0.3.2'
]

setup(
    name = "pyconfd",
    long_description=(
        '%s\n\n%s' % (
            open('README.md').read(),
            open('CHANGELOG.md').read()
        )
    ),
    package_dir={'pyconfd': 'src'},
    packages=["pyconfd", 
              "pyconfd.backends",
              "pyconfd.config",
              "pyconfd.lib"],
    scripts=["src/bin/pyconfd"],
    version=open('VERSION').read().strip(),
    description = "Python version of confd with support for etcd and environment variable backends.",
    author = "Gregory Durham",
    author_email = "gregory.durham@gmail.com",
    include_package_data=True,
    install_requires=requires
    )
