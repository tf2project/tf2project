# Terraform Test Framework
# https://github.com/tf2project/tf2project

import pytest

from tf2 import TerraformObject, TerraformObjectParser


def test_terraform_object():
    terraform_object = TerraformObject()
    assert hasattr(terraform_object, "_is_testable") is True
    assert hasattr(terraform_object, "is_testable") is True
    assert terraform_object.is_testable() is True


def test_terraform_object_parser():
    terraform_object_parser = TerraformObjectParser(
        {
            "test_string": "tf2project",
            "test_number": 10,
            "test_boolean": True,
            "test_list": [10, 20, 30],
            "test_list_object": [{"testkey": "testvalue"}],
            "test_object": {
                "testkey1": "yes",
                "testkey2": 10,
                "testkey3": [10, 20, 30],
                "testkey4": {"outside": False},
            },
        }
    )
    assert issubclass(TerraformObjectParser, TerraformObject) is True
    assert isinstance(terraform_object_parser, TerraformObjectParser) is True
    assert isinstance(terraform_object_parser, TerraformObject) is True
    assert hasattr(terraform_object_parser, "_is_testable") is True
    assert hasattr(terraform_object_parser, "is_testable") is True
    assert terraform_object_parser.is_testable() is True
    assert terraform_object_parser.test_string == "tf2project"
    assert terraform_object_parser.test_number == 10
    assert terraform_object_parser.test_boolean is True
    assert terraform_object_parser.test_list == [10, 20, 30]
    assert terraform_object_parser.test_list_object[0].testkey == "testvalue"
    assert terraform_object_parser.test_object.testkey1 == "yes"
    assert terraform_object_parser.test_object.testkey2 == 10
    assert terraform_object_parser.test_object.testkey3 == [10, 20, 30]
    assert terraform_object_parser.test_object.testkey4.outside is False
