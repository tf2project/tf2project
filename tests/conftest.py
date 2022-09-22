# Terraform Test Framework
# https://github.com/tf2project/tf2project

from os import environ
from os.path import abspath

import pytest

from tf2 import Terraform, TerraformPlanLoader, TerraformStateLoader

TF_CLI_VERSION = environ.get("TF_CLI_VERSION", None)


@pytest.fixture
def terraform_version():
    return TF_CLI_VERSION


@pytest.fixture
def terraform_tfplan_file_path(terraform_version):
    return abspath(f"./artifacts/terraform-v{ terraform_version }.tfplan.test")


@pytest.fixture
def terraform_tfstate_file_path(terraform_version):
    return abspath(f"./artifacts/terraform-v{ terraform_version }.tfstate.test")


@pytest.fixture
def terraform_tfplan_instance(terraform_tfplan_file_path):
    return Terraform(TerraformPlanLoader(terraform_tfplan_file_path))


@pytest.fixture
def terraform_tfstate_instance(terraform_tfstate_file_path):
    return Terraform(TerraformStateLoader(terraform_tfstate_file_path))
