# Terraform Test Framework
# https://github.com/tf2project/tf2project


class Test:
    def __init__(
        self,
        object_name,
        object_instance,
        test_func,
        ignore_errors,
    ):
        self.object_name = object_name
        self.object_instance = object_instance
        self.test_func = test_func
        self.ignore_errors = ignore_errors

    def get(self, name):
        return getattr(self, name, None)

    def set(self, name, value):
        setattr(self, name, value)
