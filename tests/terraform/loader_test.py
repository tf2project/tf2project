# Terraform Test Framework
# https://github.com/tf2project/tf2project

import pytest

from tf2 import TerraformLoader


def test_terraform_loader():
    terraform_loader = TerraformLoader()
    assert hasattr(terraform_loader, "_is_loader") is True
    assert hasattr(terraform_loader, "_loader_type") is True
    assert hasattr(terraform_loader, "_data_path") is True
    assert hasattr(terraform_loader, "load") is True
    assert hasattr(terraform_loader, "is_loader") is True
    assert hasattr(terraform_loader, "get_loader_type") is True
    assert hasattr(terraform_loader, "get_data_path") is True
    assert terraform_loader.is_loader() is True
    assert terraform_loader.get_loader_type() is None
    assert terraform_loader.get_data_path() is None
    with pytest.raises(Exception) as e:
        terraform_loader.load()
        assert e == "Method is not implemented."
