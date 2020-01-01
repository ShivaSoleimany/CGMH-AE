import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

__version__ = None
exec(open('cgmh_ae/version.py').read())

setup(
    name='cgmh_ae',
    version=__version__,
    packages=find_packages(exclude=(
        'dist', 'utils', 'build')),
    install_requires=reqs.strip().split('\n'),
    description="Paraphrase Generation",
    author='',
    author_email='',
    license='',
    keywords="nlp machine-learning",
    url="",
)
