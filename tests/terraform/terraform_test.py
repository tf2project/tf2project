# Terraform Test Framework
# https://github.com/tf2project/tf2project

import pytest

from tf2 import Terraform, TerraformPlanLoader, TerraformStateLoader


def test_terraform_tfplan_data(terraform_tfplan_file_path):
    terraform = Terraform(TerraformPlanLoader(terraform_tfplan_file_path))
    assert hasattr(terraform, "_data") is True
    assert hasattr(terraform, "_loader_instance") is True
    assert hasattr(terraform, "_load_data") is True
    assert hasattr(terraform, "_fetch_target_values") is True
    assert hasattr(terraform, "_parse_modules") is True
    assert hasattr(terraform, "_parse_outputs") is True
    assert hasattr(terraform, "get_loader_instance") is True
    assert hasattr(terraform, "get_data") is True
    assert terraform.get_loader_instance() is terraform._loader_instance
    assert terraform.get_data()["format_version"] == "1.1"
    assert hasattr(terraform, "resources") is True
    assert hasattr(terraform, "modules") is True
    assert hasattr(terraform, "outputs") is True
    ################### Terraform Resources Tests ####################
    assert terraform.resources.null_resource.test1.values.triggers is None
    assert terraform.resources.null_resource.test2.values.triggers is None
    assert type(terraform.resources.null_resource.test_count.instances) is list
    assert len(terraform.resources.null_resource.test_count.instances) == 2
    assert (
        terraform.resources.null_resource.test_count.instances[0].values.triggers
        is None
    )
    assert (
        terraform.resources.null_resource.test_count.instances[1].values.triggers
        is None
    )
    assert type(terraform.resources.null_resource.test_for_each.instances) is dict
    assert len(terraform.resources.null_resource.test_for_each.instances) == 2
    assert (
        terraform.resources.null_resource.test_for_each.instances[
            "test_for_each1"
        ].values.triggers
        is None
    )
    assert (
        terraform.resources.null_resource.test_for_each.instances[
            "test_for_each2"
        ].values.triggers
        is None
    )
    assert terraform.resources.random_integer.test_number.values.min == 10
    assert terraform.resources.random_integer.test_number.values.max == 20
    assert terraform.resources.random_string.test_string.values.length == 8
    assert terraform.resources.random_password.test_password.values.length == 8
    assert terraform.resources.local_file.test1.values.filename == "test1.log"
    assert (
        terraform.resources.local_file.test1.values.content == "Test 1 from Terraform"
    )
    assert terraform.resources.local_file.test2.values.filename == "test2.log"
    assert (
        terraform.resources.local_file.test2.values.content == "Test 2 from Terraform"
    )
    #################### Terraform Modules Tests #####################
    assert (
        terraform.modules.test_earth.resources.local_file.test.values.content
        == "Hello Earth"
    )
    assert (
        terraform.modules.test_moon.resources.local_file.test.values.content
        == "Hello Moon"
    )
    #################### Terraform Outputs Tests #####################
    assert terraform.outputs.test_number.sensitive is False
    assert terraform.outputs.test_number.type == "int"
    assert terraform.outputs.test_number.value == 10
    assert terraform.outputs.test_string.sensitive is False
    assert terraform.outputs.test_string.type == "str"
    assert terraform.outputs.test_string.value == "test"
    assert terraform.outputs.test_boolean.sensitive is False
    assert terraform.outputs.test_boolean.type == "bool"
    assert terraform.outputs.test_boolean.value == True
    assert terraform.outputs.test_list.sensitive is False
    assert terraform.outputs.test_list.type == "list"
    assert terraform.outputs.test_list.value == ["test1", "test2"]
    assert terraform.outputs.test_object.sensitive is False
    assert terraform.outputs.test_object.type == "dict"
    assert terraform.outputs.test_object.value.testkey == "testvalue"
    assert terraform.outputs.test_password.sensitive is True
    assert terraform.outputs.test_password.type is None
    assert terraform.outputs.test_password.value is None
    assert terraform.outputs.test_earth_output.sensitive is False
    assert terraform.outputs.test_earth_output.type == "str"
    assert terraform.outputs.test_earth_output.value == "earth.log"
    assert terraform.outputs.test_moon_output.sensitive is False
    assert terraform.outputs.test_moon_output.type == "str"
    assert terraform.outputs.test_moon_output.value == "moon.log"


def test_terraform_tfstate_data(terraform_tfstate_file_path):
    terraform = Terraform(TerraformStateLoader(terraform_tfstate_file_path))
    assert hasattr(terraform, "_data") is True
    assert hasattr(terraform, "_loader_instance") is True
    assert hasattr(terraform, "_load_data") is True
    assert hasattr(terraform, "_fetch_target_values") is True
    assert hasattr(terraform, "_parse_modules") is True
    assert hasattr(terraform, "_parse_outputs") is True
    assert hasattr(terraform, "get_loader_instance") is True
    assert hasattr(terraform, "get_data") is True
    assert terraform.get_loader_instance() is terraform._loader_instance
    assert terraform.get_data()["format_version"] == "1.0"
    assert hasattr(terraform, "data") is True
    assert hasattr(terraform, "resources") is True
    assert hasattr(terraform, "modules") is True
    assert hasattr(terraform, "outputs") is True
    ###################### Terraform Data Tests ######################
    assert (
        terraform.data.local_file.test_data_resource.values.filename == "testdata.txt"
    )
    assert (
        terraform.data.local_file.test_data_resource.values.content
        == "Terraform Test Framework\nFor test Terraform Data Resource\nhttps://tf2project.io\n"
    )
    ################### Terraform Resources Tests ####################
    assert terraform.resources.null_resource.test1.values.triggers is None
    assert terraform.resources.null_resource.test2.values.triggers is None
    assert type(terraform.resources.null_resource.test_count.instances) is list
    assert len(terraform.resources.null_resource.test_count.instances) == 2
    assert (
        terraform.resources.null_resource.test_count.instances[0].values.triggers
        is None
    )
    assert (
        terraform.resources.null_resource.test_count.instances[1].values.triggers
        is None
    )
    assert type(terraform.resources.null_resource.test_for_each.instances) is dict
    assert len(terraform.resources.null_resource.test_for_each.instances) == 2
    assert (
        terraform.resources.null_resource.test_for_each.instances[
            "test_for_each1"
        ].values.triggers
        is None
    )
    assert (
        terraform.resources.null_resource.test_for_each.instances[
            "test_for_each2"
        ].values.triggers
        is None
    )
    assert terraform.resources.random_integer.test_number.values.min == 10
    assert terraform.resources.random_integer.test_number.values.max == 20
    assert terraform.resources.random_string.test_string.values.length == 8
    assert terraform.resources.random_password.test_password.values.length == 8
    assert terraform.resources.local_file.test1.values.filename == "test1.log"
    assert (
        terraform.resources.local_file.test1.values.content == "Test 1 from Terraform"
    )
    assert terraform.resources.local_file.test2.values.filename == "test2.log"
    assert (
        terraform.resources.local_file.test2.values.content == "Test 2 from Terraform"
    )
    ############## Terraform Resources After Apply Tests #############
    assert len(terraform.resources.random_string.test_string.values.result) == 8
    assert len(terraform.resources.random_password.test_password.values.result) == 8
    #################### Terraform Modules Tests #####################
    assert (
        terraform.modules.test_earth.resources.local_file.test.values.content
        == "Hello Earth"
    )
    assert (
        terraform.modules.test_moon.resources.local_file.test.values.content
        == "Hello Moon"
    )
    #################### Terraform Outputs Tests #####################
    assert terraform.outputs.test_number.sensitive is False
    assert terraform.outputs.test_number.type == "int"
    assert terraform.outputs.test_number.value == 10
    assert terraform.outputs.test_string.sensitive is False
    assert terraform.outputs.test_string.type == "str"
    assert terraform.outputs.test_string.value == "test"
    assert terraform.outputs.test_boolean.sensitive is False
    assert terraform.outputs.test_boolean.type == "bool"
    assert terraform.outputs.test_boolean.value == True
    assert terraform.outputs.test_list.sensitive is False
    assert terraform.outputs.test_list.type == "list"
    assert terraform.outputs.test_list.value == ["test1", "test2"]
    assert terraform.outputs.test_object.sensitive is False
    assert terraform.outputs.test_object.type == "dict"
    assert terraform.outputs.test_object.value.testkey == "testvalue"
    assert terraform.outputs.test_password.sensitive is True
    assert terraform.outputs.test_password.type == "str"
    assert len(terraform.outputs.test_password.value) == 8
    assert terraform.outputs.test_earth_output.sensitive is False
    assert terraform.outputs.test_earth_output.type == "str"
    assert terraform.outputs.test_earth_output.value == "earth.log"
    assert terraform.outputs.test_moon_output.sensitive is False
    assert terraform.outputs.test_moon_output.type == "str"
    assert terraform.outputs.test_moon_output.value == "moon.log"