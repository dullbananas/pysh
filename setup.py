#!/usr/bin/env python3.7

from setuptools import setup

with open('README.md', 'r') as f:
	readme = f.read()

setup(
	name='shellp',
	version='0.0.0',
	description='An advanced shell',
	long_description=readme,
	long_description_content_type='text/markdown',
	author='Dull Bananas',
	author_email='dull.bananas0@gmail.com',
	url='https://github.com/dullbananas/shellp',
	license='GPLv2',
	packages=['shellp'],
	entry_points={
		'console_scripts': [
			'shellp = shellp.__main__:run',
		],
	},
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: Console',
		'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
		'Natural Language :: English',
		'Topic :: System :: Shells',
	],
	python_requires='>=3.6',
)
