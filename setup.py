#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Jane Wyngaard",
    author_email='jane.wyngaard@uct.ac.za',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="DRS API for connecting a range of sensor types to the LANDRS data annotation toolkit",
    entry_points={
        'console_scripts': [
            'LANDRS_Sensor_API=LANDRS_Sensor_API.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='LANDRS_Sensor_API',
    name='LANDRS_Sensor_API',
    packages=find_packages(include=['LANDRS_Sensor_API', 'LANDRS_Sensor_API.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/r4space/LANDRS_Sensor_API',
    version='0.1.0',
    zip_safe=False,
)
