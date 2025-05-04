'''
The setup.py file is used in Python projects, including data science projects, to define the package 
metadata and handle installation, distribution, and dependency management. It plays a central role in 
making your code reusable, installable, and sharable (e.g., via PyPI or within a team).
'''

from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    '''
    This function reads a requirements file and returns a list of required packages.
    '''
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read all lines from the requirements file
            lines = file.readlines()
            ## Proccess the lines
            for line in lines:
                # Remove any leading/trailing whitespace characters and filter out empty lines
                requirement = line.strip()
                # ignore empty lines and '-e .' (editable install)
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
        
    return requirement_lst

print(get_requirements())

setup(
    name='NetworkSecurity',  #  project name
    version='0.0.1',  # project version
    author='Daman Kumar',
    author_email='daman.kheterpal007@gmail.com',
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=get_requirements(),  # List of dependencies
)