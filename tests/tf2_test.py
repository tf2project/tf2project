# Terraform Test Framework
# https://github.com/tf2project/tf2project

import pytest

from tf2 import Terraform, TerraformPlanLoader, TerraformStateLoader, Tf2


def test_tf2_with_plan_data(terraform_tfplan_file_path):
    tf2 = Tf2(Terraform(TerraformPlanLoader(terraform_tfplan_file_path)))
    with pytest.raises(Exception) as e:
        tf2.add_test("not_found_resource.not_found_object", lambda: True)
        assert e == "Object 'not_found_resource.not_found_object' is not available."
    with pytest.raises(Exception) as e:
        tf2.add_test("resources.random_integer.test_number.values", lambda: True)
        assert (
            e == "Object 'resources.random_integer.test_number.values' is not testable."
        )
    with pytest.raises(SystemExit) as e:
        tf2.run()

    @tf2.test("resources.random_password.test_password")
    def sample_test1(self):
        assert self.values.length >= 8

    with pytest.raises(SystemExit) as e:
        tf2.run()

    @tf2.test("resources.random_string.test_string")
    def sample_test2(self):
        assert self.values.length >= 12

    with pytest.raises(SystemExit) as e:
        tf2.run()
    tf2 = Tf2(
        terraform_instance=Terraform(TerraformPlanLoader(terraform_tfplan_file_path)),
        ignore_errors=True,
        silent_mode=True,
    )

    @tf2.test("modules.test_earth.resources.local_file.test")
    def sample_test3():
        assert (
            tf2.modules.test_earth.resources.local_file.test.values.filename
            == "earth.log"
        )

    with pytest.raises(SystemExit) as e:
        tf2.run()


def test_tf2_with_state_data(terraform_tfstate_file_path):
    tf2 = Tf2(Terraform(TerraformStateLoader(terraform_tfstate_file_path)))
    with pytest.raises(Exception) as e:
        tf2.add_test("not_found_resource.not_found_object", lambda: True)
        assert e == "Object 'not_found_resource.not_found_object' is not available."
    with pytest.raises(Exception) as e:
        tf2.add_test("resources.random_integer.test_number.values", lambda: True)
        assert (
            e == "Object 'resources.random_integer.test_number.values' is not testable."
        )
    with pytest.raises(SystemExit) as e:
        tf2.run()

    @tf2.test("resources.random_password.test_password")
    def sample_test1(self):
        assert self.values.length >= 8

    with pytest.raises(SystemExit) as e:
        tf2.run()

    @tf2.test("resources.random_string.test_string")
    def sample_test2(self):
        assert self.values.length >= 12

    with pytest.raises(SystemExit) as e:
        tf2.run()
    tf2 = Tf2(
        terraform_instance=Terraform(TerraformStateLoader(terraform_tfstate_file_path)),
        ignore_errors=True,
        silent_mode=True,
    )

    @tf2.test("modules.test_earth.resources.local_file.test")
    def sample_test3():
        assert (
            tf2.modules.test_earth.resources.local_file.test.values.filename
            == "earth.log"
        )

    with pytest.raises(SystemExit) as e:
        tf2.run()
