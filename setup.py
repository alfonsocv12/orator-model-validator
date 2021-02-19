import setuptools
import sys

if sys.version_info < (3, 0):
     raise NotImplementedError("Sorry, you need at least Python 2.7 or Python 3.4+ to use bottle.")

with open("README.rst", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    url="https://pypi.org/project/orator-validator/",
    name="orator_validator",
    version="0.5.0",
    author="Alfonso Villalobos",
    author_email="alfonso@codepeat.com",
    license='MIT',
    description="Orator Validator provides the best Model validation for Orator",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)
