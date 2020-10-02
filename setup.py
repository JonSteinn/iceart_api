#!/usr/bin/env python
import os

from setuptools import find_packages, setup


def read(fname):
    """Read file and return as string."""
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()


def get_version():
    """Grab version from the ./iceart/__init__.py file."""
    with open("iceart/__init__.py", encoding="utf-8") as init_file:
        for line in init_file.readlines():
            if line.startswith("__version__"):
                return line.split(" = ")[1].rstrip()[1:-1]
    raise ValueError("Version not found in iceart/__init__.py")


setup(
    name="iceart",
    version=get_version(),
    author="IceArtGroup",
    author_email="",
    description="Api for IceArtRecognition app",
    license="GPLv3",
    keywords=("flask api rest"),
    url="https://github.com/JonSteinn/iceart_api",
    project_urls={
        "Source": "https://github.com/JonSteinn/iceart_api",
        "Tracker": "https://github.com/JonSteinn/iceart_api/issues",
    },
    packages=find_packages(),
    long_description_content_type="text/x-rst",
    long_description=read("README.rst"),
    install_requires=["flask==1.1.1"],
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={"console_scripts": []},
)
