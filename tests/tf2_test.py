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


def test_tf2_with_all_plan_data(terraform_tfplan_file_path):
    tf2 = Tf2(Terraform(TerraformPlanLoader(terraform_tfplan_file_path)))

    @tf2.test("resources")
    def sample_test1(self):
        assert ("null_resource" in self.__all__) is True
        assert ("random_integer" in self.__all__) is True
        assert ("random_string" in self.__all__) is True
        assert ("random_password" in self.__all__) is True
        assert ("local_file" in self.__all__) is True

    @tf2.test("resources.local_file")
    def sample_test2(self):
        for resource in self.__all__:
            assert resource.values.file_permission == "0777"

    @tf2.test("modules")
    def sample_test3(self):
        assert ("test_earth" in self.__all__) is True
        assert ("test_moon" in self.__all__) is True

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


def test_tf2_with_all_state_data(terraform_tfstate_file_path):
    tf2 = Tf2(Terraform(TerraformStateLoader(terraform_tfstate_file_path)))

    @tf2.test("data")
    def sample_test1(self):
        assert ("local_file" in self.__all__) is True

    @tf2.test("data.local_file")
    def sample_test2(self):
        for data in self.__all__:
            assert resource.values.file_permission == "0777"

    @tf2.test("resources")
    def sample_test3(self):
        assert ("null_resource" in self.__all__) is True
        assert ("random_integer" in self.__all__) is True
        assert ("random_string" in self.__all__) is True
        assert ("random_password" in self.__all__) is True
        assert ("local_file" in self.__all__) is True

    @tf2.test("resources.local_file")
    def sample_test4(self):
        for resource in self.__all__:
            assert resource.values.file_permission == "0777"

    @tf2.test("modules")
    def sample_test5(self):
        assert ("test_earth" in self.__all__) is True
        assert ("test_moon" in self.__all__) is True

    with pytest.raises(SystemExit) as e:
        tf2.run()
