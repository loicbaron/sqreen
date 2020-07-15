# -*- coding: utf-8 -*-
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='project',
        version='0.1',
        description='Sqreen Notifications Backend',
        long_description=long_description,
        url='https://github.com/loicbaron/sqreen',
        author=u'loicbaron',
        author_email='loic.baron@gmail.com',
        license='MIT',
        packages=['project'],
        include_package_data=True,
        install_requires=[
            'flask',
        ],
        classifiers=[
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            'Development Status :: 3 - Alpha',

            # Indicate who your project is intended for
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',

            # Pick your license as you wish (should match "license" above)
            "License :: OSI Approved :: MIT License",

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        keywords='project backend flask',
)