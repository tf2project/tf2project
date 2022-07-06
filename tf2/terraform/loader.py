# Terraform Test Framework
# https://github.com/tf2project/tf2

from json import loads as load_json
from os.path import exists
from subprocess import run as run_subprocess


class TerraformLoader:
    def __init__(self, terraform_file_path):
        self._is_loader = True
        self._terraform_file_path = terraform_file_path

    def load(self):
        if exists(self._terraform_file_path) is False:
            raise Exception(f"File '{ self._terraform_file_path }' is not found.")
        result = run_subprocess(
            ["terraform", "show", "-json", self._terraform_file_path],
            capture_output=True,
        )
        try:
            return load_json(result.stdout)
        except:
            raise Exception(
                f"File '{ self._terraform_file_path }' could not be loaded."
            )


class TerraformPlanLoader(TerraformLoader):
    def __init__(self, plan_file_path=None):
        self.loader_type = "planloader"
        if plan_file_path is None:
            self._plan_file_path = "./terraform.tfplan"
        else:
            self._plan_file_path = plan_file_path
        super().__init__(self._plan_file_path)


class TerraformStateLoader(TerraformLoader):
    def __init__(self, state_file_path=None):
        self.loader_type = "stateloader"
        if state_file_path is None:
            self._state_file_path = "./terraform.tfstate"
        else:
            self._state_file_path = state_file_path
        super().__init__(self._state_file_path)
