# Terraform Test Framework
# https://github.com/tf2project/tf2project


class Executor:
    def __init__(self):
        self._is_executor = True
        self._is_complete = False
        self.result = None

    def is_executor(self):
        return self._is_executor

    def is_complete(self):
        return self._is_complete

    def execute(self):
        raise Exception("Method is not implemented.")

    def _set_result(self, **data):
        self.result = self.Result(**data)

    class Result:
        def __init__(self, **data):
            self.__dict__.update(data)
