# Terraform Test Framework
# https://github.com/tf2project/tf2project

import pytest

from tf2.terraform import get_attr_name, get_output_type


def test_get_output_type():
    assert get_output_type("test") == "str"
    assert get_output_type(10) == "int"
    assert get_output_type([10, 20, 30]) == "list"
    assert get_output_type({"testkey": "testvalue"}) == "dict"
    assert get_output_type(True) == "bool"


def test_get_attr_name():
    assert get_attr_name("app.tf2project.io/name") == "app_tf2project_io_name"
    assert get_attr_name("test_key") == "test_key"
    assert get_attr_name("__test__key__") == "_test_key_"
