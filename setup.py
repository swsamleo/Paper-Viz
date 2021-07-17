import os
from setuptools import setup, find_packages

# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Paper-Viz',
    version='1.0.0',
    description='Professional Python Graphs for Scientific Papers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/swsamleo/Paper-Viz',
    author='CRUISE Group',
    author_email='wei.shao@rmit.edu.au',
    license='GNU GPLv3',
    classfiers=[
        'Programming Language :: Python :: 3',
    ],
    keywords=[
        'scientific papers',
        'professional python graphs'
        'thesis template'
        'python'
    ],
    packages=find_packages(),
    include_package_data=True,
)
