# Terraform Test Framework
# https://github.com/tf2project/tf2project

from sys import exit
from time import perf_counter

from .cli import print_run_footer, print_run_header, print_test_result
from .terraform import Terraform
from .test import Test


class Tf2:
    def __init__(
        self,
        terraform_instance=None,
        ignore_errors=False,
        silent_mode=False,
        create_result_file=True,
    ):
        if terraform_instance is None:
            self._terraform_instance = Terraform()
        else:
            self._terraform_instance = terraform_instance
        self._ignore_errors = ignore_errors
        self._silent_mode = silent_mode
        self._create_result_file = create_result_file
        self._fetch_objects()
        self._tests = []

    def _fetch_objects(self):
        for object_name in ["resources", "data", "modules", "outputs"]:
            if hasattr(self._terraform_instance, object_name):
                setattr(
                    self,
                    object_name,
                    getattr(self._terraform_instance, object_name),
                )

    def _find_testable_object(self, object_name):
        current_object = self
        target_object_tree = object_name.split(".")
        for target_object_name in target_object_tree:
            if hasattr(current_object, target_object_name) is False:
                raise Exception(f"Object '{ object_name }' is not available.")
            target_object = getattr(current_object, target_object_name)
            if target_object.is_testable() is False:
                raise Exception(f"Object '{ object_name }' is not testable.")
            current_object = target_object
        return current_object

    def add_test(self, object_name, test_func, ignore_errors=None):
        self._tests.append(
            Test(
                object_name=object_name,
                object_instance=self._find_testable_object(object_name),
                test_func=test_func,
                ignore_errors=self._ignore_errors
                if ignore_errors is None
                else ignore_errors,
            )
        )

    def test(self, object_name, ignore_errors=None):
        test_wrapper = lambda test_func: self.add_test(
            object_name, test_func, ignore_errors
        )
        return test_wrapper

    def run(self):
        if self._silent_mode is False:
            print_run_header(
                self._terraform_instance.get_data()["terraform_version"],
                self._terraform_instance.get_data()["format_version"],
                self._terraform_instance.get_loader_instance().get_loader_type(),
                self._terraform_instance.get_loader_instance().get_data_path(),
                len(self._tests),
            )
        total_passed_tests = total_failed_tests = 0
        overall_result = True
        start_time = perf_counter()
        for test in self._tests:
            current_test_result = True
            try:
                if "self" in test.test_func.__code__.co_varnames:
                    test.test_func(test.object_instance)
                else:
                    test.test_func()
            except:
                current_test_result = False
            if current_test_result is True:
                total_passed_tests += 1
            else:
                total_failed_tests += 1
                if test.ignore_errors is False:
                    overall_result = False
            if self._silent_mode is False:
                print_test_result(
                    test.object_name,
                    test.test_func.__name__,
                    current_test_result,
                )
            if current_test_result is False and test.ignore_errors is False:
                break
        total_time = perf_counter() - start_time
        if self._silent_mode is False:
            print_run_footer(
                overall_result,
                total_failed_tests,
                total_passed_tests,
                total_time,
            )
        if self._create_result_file is True:
            with open(".tf2result", "w") as f:
                f.write("passed") if overall_result else f.write("failed")
                f.write("\n")
        exit(not overall_result)
