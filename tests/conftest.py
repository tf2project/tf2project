# Terraform Test Framework
# https://github.com/tf2project/tf2project

from os import environ
from os.path import abspath

import pytest

TF_CLI_VERSION = environ.get("TF_CLI_VERSION", "1.2.7")


@pytest.fixture
def terraform_version():
    return TF_CLI_VERSION


@pytest.fixture
def terraform_tfplan_file_path(terraform_version):
    return abspath(f"./artifacts/terraform-v{ terraform_version }.tfplan.test")


@pytest.fixture
def terraform_tfstate_file_path(terraform_version):
    return abspath(f"./artifacts/terraform-v{ terraform_version }.tfstate.test")
