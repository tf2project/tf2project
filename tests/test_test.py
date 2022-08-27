# Terraform Test Framework
# https://github.com/tf2project/tf2project

import pytest

from tf2 import Test


def test_test():
    test = Test("test", object(), len, True)
    assert hasattr(test, "object_name") is True
    assert hasattr(test, "object_instance") is True
    assert hasattr(test, "test_func") is True
    assert hasattr(test, "ignore_errors") is True
    assert hasattr(test, "get") is True
    assert hasattr(test, "set") is True
    assert test.object_name == "test"
    assert isinstance(test.object_instance, object) is True
    assert test.test_func is len
    assert test.ignore_errors is True
    assert test.get("object_name") == "test"
    test.set("test_key", "test_value")
    assert hasattr(test, "test_key") is True
    assert test.test_key == "test_value"
