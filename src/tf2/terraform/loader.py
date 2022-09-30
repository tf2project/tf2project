# Terraform Test Framework
# https://github.com/tf2project/tf2project


class TerraformLoader:
    def __init__(self):
        self._is_loader = True
        self._loader_type = None
        self._data_path = None

    def load(self):
        raise Exception("Method is not implemented.")

    def is_loader(self):
        return self._is_loader

    def get_loader_type(self):
        return self._loader_type

    def get_data_path(self):
        return self._data_path
