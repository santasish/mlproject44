from setuptools import find_packages, setup
from typing import List
import os

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''The function returns a list of requirements'''
    requirements = []
    abs_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(abs_path) as file_obj:
        requirements = [
            req.strip() for req in file_obj.readlines()
            if req.strip() and not req.startswith("#")
        ]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject44',
    version='0.0.1',
    author='Santasish',
    author_email='infosantasish@gmail.com',
    description='A machine learning project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/santasish/mlproject44',  # Replace with your repository URL
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)