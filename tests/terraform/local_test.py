# Terraform Test Framework
# https://github.com/tf2project/tf2project

from os import getcwd
from os.path import join

import pytest

from tf2.terraform.loader import TerraformLoader
from tf2.terraform.local import *


def test_terraform_local_file_loader():
    terraform_local_file_loader = TerraformLocalFileLoader(".tf2notfound")
    assert issubclass(TerraformLocalFileLoader, TerraformLoader) is True
    assert isinstance(terraform_local_file_loader, TerraformLoader) is True
    assert hasattr(terraform_local_file_loader, "_is_loader") is True
    assert hasattr(terraform_local_file_loader, "_loader_type") is True
    assert hasattr(terraform_local_file_loader, "_data_path") is True
    assert hasattr(terraform_local_file_loader, "load") is True
    assert hasattr(terraform_local_file_loader, "is_loader") is True
    assert hasattr(terraform_local_file_loader, "get_loader_type") is True
    assert hasattr(terraform_local_file_loader, "get_data_path") is True
    assert terraform_local_file_loader.is_loader() is True
    assert terraform_local_file_loader.get_loader_type() is None
    assert terraform_local_file_loader.get_data_path() == join(getcwd(), ".tf2notfound")
    with pytest.raises(Exception) as e:
        terraform_local_file_loader.load()
        assert e == f"File '{ terraform_local_file_loader._data_path }' is not found."
    with pytest.raises(Exception) as e:
        terraform_local_file_loader = TerraformLocalFileLoader("/proc/self/cmdline")
        terraform_local_file_loader.load()
        assert (
            e
            == f"File '{ terraform_local_file_loader._data_path }' could not be loaded."
        )


def test_terraform_plan_loader(terraform_version, terraform_tfplan_file_path):
    terraform_plan_loader = TerraformPlanLoader(terraform_tfplan_file_path)
    assert issubclass(TerraformPlanLoader, TerraformLocalFileLoader) is True
    assert isinstance(terraform_plan_loader, TerraformLocalFileLoader) is True
    terraform_json_data = terraform_plan_loader.load()
    assert terraform_json_data["format_version"] == "1.1"
    assert terraform_json_data["terraform_version"] == terraform_version
    assert ("planned_values" in terraform_json_data) is True


def test_terraform_state_loader(terraform_version, terraform_tfstate_file_path):
    terraform_state_loader = TerraformStateLoader(terraform_tfstate_file_path)
    assert issubclass(TerraformStateLoader, TerraformLocalFileLoader) is True
    assert isinstance(terraform_state_loader, TerraformLocalFileLoader) is True
    terraform_json_data = terraform_state_loader.load()
    assert terraform_json_data["format_version"] == "1.0"
    assert terraform_json_data["terraform_version"] == terraform_version
    assert ("values" in terraform_json_data) is True
