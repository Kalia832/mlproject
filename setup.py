from setuptools import find_packages,setup
from typing import List

HYPEN_DOT_E='-e .'
def get_requiremetns(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Kalia',
author_email='kalia.contact.2022@gmail.com',
packages=find_packages(),
install_requires=get_requiremetns('requirements.txt')

)