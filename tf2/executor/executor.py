# Terraform Test Framework
# https://github.com/tf2project/tf2project


class Executor:
    def __init__(self):
        self._is_executor = True


class ExecutorResult:
    def __init__(self, **kwargs):
        self._is_result = True
        self.__dict__.update(kwargs)
