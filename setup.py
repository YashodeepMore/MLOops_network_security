""" setup.py file is the essential part of packaging and distributing the python project.
It od used by setup tools (distutils in older version of python ) to define the confreigustion of project ,
such as its metadata, dependencies and more """

from setuptools import find_packages, setup
from typing import List
def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirements_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e .":
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print('rewuirement.txt file not found')

    return requirements_list

setup(
    name="Network_Security",
    version="0.0.1",
    author="Yashodeep More",
    author_email="yashodeepmore01@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)