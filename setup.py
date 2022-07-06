# Terraform Test Framework
# https://github.com/tf2project/tf2

from os import environ

from setuptools import setup

from tf2 import __version__

if environ.get("ENV", "production") == "development":
    with open("requirements.txt") as f:
        requirements = f.readlines()
else:
    requirements = []

setup(
    name="tf2",
    description="Terraform Test Framework",
    author="Saeid Bostandoust",
    author_email="ssbostan@yahoo.com",
    version=__version__,
    install_requires=requirements,
    include_package_data=False,
    zip_safe=True,
)
