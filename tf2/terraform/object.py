# Terraform Test Framework
# https://github.com/tf2project/tf2project

from .util import get_attr_name


class TerraformObject:
    def __init__(self, is_testable=True):
        self._is_testable = is_testable

    def is_testable(self):
        return self._is_testable


class TerraformObjectParser(TerraformObject):
    def __init__(self, data, is_testable=True):
        super().__init__(is_testable)
        for _key, value in data.items():
            key = get_attr_name(_key)
            if isinstance(value, dict) is True:
                setattr(self, key, TerraformObjectParser(value, False))
            elif isinstance(value, (list, tuple)) is True:
                items = [
                    TerraformObjectParser(item, False)
                    if isinstance(item, dict)
                    else item
                    for item in value
                ]
                setattr(self, key, items)
            else:
                setattr(self, key, value)
