# Terraform Test Framework
# https://github.com/tf2project/tf2

from importlib.metadata import version as package_version
from os import get_terminal_size, getcwd
from os.path import abspath
from platform import python_version
from platform import system as system_version

RUN_HEADER = """\033[1m{0}\033[0m
   __________   ________    _______
  |\___   ___\ |\  _____\  /  ___  \\
  \|___ \  \_| \ \  \__/  /__/|_/  /|
       \ \  \   \ \   __\ |__|//  / /
        \ \  \   \ \  \_|     /  /_/__
         \ \__\   \ \__\     |\________\\
          \|__|    \|__|     \|________| Terraform Test Framework

platform {1}, python {2}
tf2 {3}, terraform {4}, json {5}, type {6}
rootdir: {7}
file: {8}
\033[1mcollected {9} {10}\033[0m
"""

RUN_FOOTER = """{0}\033[1m{1}\033[0m{2}"""

TEST_RESULT = """object_name: \033[1m{0}\033[0m
\u2799 test_func: \033[1m{1}\033[0m {2} \033[1m{3}\033[0m
"""


def create_fullwidth_line(input_string):
    available_columns = get_terminal_size().columns - len(input_string)
    available_columns = 4 if available_columns < 4 else available_columns
    left_available_columns = available_columns // 2
    right_available_columns = available_columns // 2 + available_columns % 2
    return "".join(
        (
            "=" * (left_available_columns - 1),
            " ",
            input_string,
            " ",
            "=" * (right_available_columns - 1),
        )
    )


def print_test_result(object_name, test_func, test_result):
    print(
        TEST_RESULT.format(
            object_name,
            test_func,
            "\u2705" if test_result else "\u274c",
            "\033[92mPASSED" if test_result else "\033[91mFAILED",
        )
    )


def print_run_header(
    terraform_version,
    format_version,
    loader_type,
    terraform_file_path,
    total_tests,
):
    print(
        RUN_HEADER.format(
            create_fullwidth_line("tf2"),
            system_version().lower(),
            python_version(),
            package_version("tf2"),
            terraform_version,
            format_version,
            loader_type,
            getcwd(),
            abspath(terraform_file_path),
            total_tests,
            "tests" if total_tests > 1 else "test",
        )
    )


def print_run_footer(
    overall_result,
    total_failed_tests,
    total_passed_tests,
    total_time,
):
    output = ""
    if total_failed_tests:
        output += f"{total_failed_tests} failed "
    if total_passed_tests:
        output += f"{total_passed_tests} passed "
    if not total_failed_tests and not total_passed_tests:
        output += "nothing "
    output += f"in {round(total_time, 2)}s"
    print(
        RUN_FOOTER.format(
            "\033[92m" if overall_result else "\033[91m",
            create_fullwidth_line(output),
            "\033[0m",
        )
    )
