#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

package_name = 'launch_examples'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(
        exclude=['doc*', 'tests*', 'graveyard*', 'scripts*']
    ),
    data_files=[
        ('share/' + package_name,
         [
             'pub_sub.launch.py',
             'package.xml',
             'testies.launch.py',
          ]
         ),
    ],
    package_data={},
    install_requires=[],
    extras_require={},
    author='Daniel Stonier',
    maintainer='Daniel Stonier <d.stonier@gmail.com>',
    url='https://github.com/stonier/launch_examples',
    keywords=['ROS'],
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    description=(
        "ROS2 launch examples."
    ),
    long_description=(
        "ROS2 launch examples."
    ),
    license='BSD',
    # test_suite='tests',
    # tests_require=[],  # using vanilla py unit tests
    # entry_points={
    #     'console_scripts': [
    #        'py-trees-blackboard-watcher = launch_examples.programs.blackboard_watcher:main',
    #     ],
    # },
)
