from pathlib import Path
from setuptools import setup
from setuptools import find_packages

version = "0.0.1"
description = "Python tools to help build the MarkSTAT - a global trade mark dataset."

source_root = Path(".")

with (source_root / "README.md").open(encoding="utf-8") as fh:
    long_description = fh.read()

with (source_root / "requirements.txt").open(encoding="utf-8") as f:
    requirements = f.readlines()

setup(
    name="markstattools",
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Min Chul Kim",
    author_email="minchulkim87@gmail.com",
    url="https://minchulkim87.github.io/markstattools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy==1.18.3",
        "pandas==1.0.3",
        "pyarrow==0.17.0",
        "python-dateutil==2.8.1",
        "pytz==2020.1",
        "six==1.14.0",
        "xmltodict==0.12.0",
    ]
)
