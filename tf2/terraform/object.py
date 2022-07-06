# Terraform Test Framework
# https://github.com/tf2project/tf2


class TerraformObject:
    def __init__(self, testable=True):
        self.testable = testable


class TerraformObjectParser(TerraformObject):
    def __init__(self, data, testable=True):
        super().__init__(testable)
        # FIXME: if the key consists of dashes, it will be cracked.
        for key, value in data.items():
            if isinstance(value, dict) is True:
                setattr(self, key, TerraformObjectParser(value, testable=False))
            elif isinstance(value, (list, tuple)) is True:
                items = [
                    TerraformObjectParser(item, testable=False)
                    if isinstance(item, dict)
                    else item
                    for item in value
                ]
                setattr(self, key, items)
            else:
                setattr(self, key, value)
