#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import platform

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'stm32loader', 'pyserial', 'appdirs', 'requests']

if 'armv7l' in platform.machine() :
    requirements.append('Adafruit_BBIO')

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Alexis Jeandet",
    author_email='alexis.jeandet@member.fsf.org',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A LPP's BBone sensor cape manager",
    entry_points={
        'console_scripts': [
            'bbone_sensors=bbone_sensors.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bbone_sensors',
    name='bbone_sensors',
    packages=find_packages(include=['bbone_sensors', 'bbone_sensors.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jeandet/bbone_sensors',
    version='0.1.0',
    zip_safe=False,
)
