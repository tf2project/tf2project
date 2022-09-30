#!/usr/bin/bash

# Terraform Test Framework
# https://github.com/tf2project/tf2project

isort --py 310 src tests
black -t py310 src tests
