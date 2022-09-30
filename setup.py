# Terraform Test Framework
# https://github.com/tf2project/tf2project

from os import environ

from setuptools import setup

if environ.get("ENV", "production") == "development":
    with open("requirements.txt") as f:
        requirements = f.readlines()
else:
    requirements = []

with open("README.md") as f:
    readme = f.read()

setup(
    long_description=readme,
    install_requires=requirements,
)
