# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in aartisteel/__init__.py
from aartisteel import __version__ as version

setup(
	name='aartisteel',
	version=version,
	description='Steel Manufacturing',
	author='Atriina Technologies',
	author_email='developers@atriina.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
