from setuptools import find_packages,setup

from typing import List

HYPEN_E_Dot = '-e .'

def get_requirements(filepath: str) -> list[str]:
    '''
    this function will return the list of requirements

    '''
    requirements = []
    with open(filepath, ) as file_obj:
        requirements =file_obj.readlines()
        requirements = [req.replace("\n","n") for req in requirements]
        
        if HYPEN_E_Dot in requirements:
            requirements.remove(HYPEN_E_Dot)


setup(
    name='mlproject',
    version='0.0.1',
    email='anandmehta300@gmail.com',
    author = 'anand singh',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')

)