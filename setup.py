# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in customer_rewards/__init__.py
from customer_rewards import __version__ as version

setup(
	name='customer_rewards',
	version=version,
	description='Customer referrals',
	author='Tridz',
	author_email='example@tridz.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
