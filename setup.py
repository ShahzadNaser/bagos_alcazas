# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in alcazas/__init__.py
from alcazas import __version__ as version

setup(
	name='alcazas',
	version=version,
	description='Alcazas',
	author='Alcazas',
	author_email='alzadmin@alz-group.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
