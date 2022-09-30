# Terraform Test Framework
# https://github.com/tf2project/tf2project

from re import match, sub


def get_output_type(value):
    return match("<class '(.*)'>", str(type(value)))[1]


def get_attr_name(value):
    for pattern in ["\W", "_+"]:
        value = sub(pattern, "_", value)
    return value
