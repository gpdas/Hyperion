#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = '2.0.0-alpha'

setup(
    name='hyperion',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hyperion=hyperion:main',
        ],
    },

    package_data={
        # Include any files found in the 'scripts' subdirectory
        '': ['bin/*', 'data/*'],
    },

    version=VERSION,
    install_requires=['libtmux',
                      'pyyaml',
                      'psutil',
                      'enum34',
                      'selectors2;python_version<"3.4"'],
    extras_require={
        'GRAPH': ['graphviz'],
        'I-CLI': ['urwid'],
        'FULL': ['graphviz', 'urwid']
    },

    description='The Hyperion Launch Engine',
    author='David Leins',
    author_email='dleins@techfak.uni-bielefeld.de',
    url='https://github.com/DavidPL1/Hyperion.git',
    keywords=['libtmux'],
    classifiers=[],
    include_package_data=True,
    zip_safe=False
)
