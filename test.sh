#!/usr/bin/bash

# Terraform Test Framework
# https://github.com/tf2project/tf2project

export TF_CLI_CHDIR="$(pwd)/artifacts"

coverage run -m pytest
coverage html
coverage xml
