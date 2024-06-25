from setuptools import find_packages, setup
from typing import List


def get_requirements()->list[str]:
    requirements: list[str] = []
    
    return requirements

setup(
    name = "Air Pressure system",
    version = '0.0.1',
    author="Anil Kumar",
    author_email="anilkumar01.ds@gmail.com",
    packages="find_packages()",
    install_requires = get_requirements(),
)