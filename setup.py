import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

__version__ = None
exec(open('hope/version.py').read())

with open('requirements.txt') as f:
    reqs = f.read()

setup(
    name='hope',
    version=__version__,
    packages=find_packages(exclude=(
        'dist', 'utils', 'build')),
    install_requires=reqs.strip().split('\n'),
    description="Paraphrase Generation",
    author='',
    author_email='',
    license='Apache 2.0',
    keywords="nlp machine-learning",
    url="",
)
