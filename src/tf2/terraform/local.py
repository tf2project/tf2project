# Terraform Test Framework
# https://github.com/tf2project/tf2project

from json import loads as load_json
from os import environ, getcwd
from os.path import abspath, exists
from subprocess import run as run_subprocess

from .loader import TerraformLoader

TF_CLI_CHDIR = environ.get("TF_CLI_CHDIR", getcwd())


class TerraformLocalFileLoader(TerraformLoader):
    def __init__(self, file_path):
        super().__init__()
        self._data_path = abspath(file_path)

    def load(self):
        if exists(self._data_path) is False:
            raise Exception(f"File '{ self._data_path }' is not found.")
        result = run_subprocess(
            f"terraform -chdir={ TF_CLI_CHDIR } show -json { self._data_path }",
            shell=True,
            capture_output=True,
        )
        try:
            return load_json(result.stdout)
        except:
            raise Exception(f"File '{ self._data_path }' could not be loaded.")


class TerraformPlanLoader(TerraformLocalFileLoader):
    def __init__(self, file_path=None):
        file_path = "./terraform.tfplan" if file_path is None else file_path
        super().__init__(file_path)
        self._loader_type = "planloader"


class TerraformStateLoader(TerraformLocalFileLoader):
    def __init__(self, file_path=None):
        file_path = "./terraform.tfstate" if file_path is None else file_path
        super().__init__(file_path)
        self._loader_type = "stateloader"
