#!/usr/bin/bash

# Terraform Test Framework
# https://github.com/tf2project/tf2project

isort --py 310 tf2
black -t py310 tf2
