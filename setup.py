#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""

from setuptools import setup, find_packages
from jdcloud_cli.version import VERSION

install_requires = ['websocket-client', 'configparser', 'requests',
                    'argcomplete', 'argparse', 'jdcloud_sdk==1.5.9', 'pyyaml', 'jinja2']


setup(
    name='jdcloud_cli',
    description='Universal Command Line Environment for jdcloud',
    version=VERSION,
    author='JDCloud API Gateway Team',
    url='https://github.com/jdcloud-api/jdcloud-cli',
    packages=find_packages(),
    package_data={'jdcloud_cli': ['resources/skeletons/*', 'resources/kubernetes/*']},
    platforms=['unix', 'linux', 'osx', 'win64'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'jdc = jdcloud_cli.jdc:main',
        ]
    }
)
