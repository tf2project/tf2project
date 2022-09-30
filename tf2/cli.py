# Terraform Test Framework
# https://github.com/tf2project/tf2project

from importlib.metadata import version as package_version
from os import get_terminal_size, getcwd
from platform import python_version
from platform import system as system_version

RUN_HEADER = """\033[1m{0}\033[0m
   \033[92m__________   ________    _______
  |\___   ___\ |\  _____\  /  ___  \\
  \|___ \  \_| \ \  \__/  /__/|_/  /|\033[0m
       \ \  \   \ \   __\ |__|//  / /
        \ \  \   \ \  \_|     /  /_/__
         \033[91m\ \__\   \ \__\     |\________\\ Dedicated to Iran and Iranians
          \|__|    \|__|     \|________| Terraform Test Framework\033[0m

platform {1}, python {2}
tf2 {3}, terraform {4}, json {5}, type {6}
rootdir: {7}
datapath: {8}
\033[1mcollected {9} {10}\033[0m
"""

RUN_FOOTER = """\033[1m{0}{1}\033[0m"""

OUTPUT_STRING = """{0} in {1}s"""

FULLWIDTH_LINE = """{0} {1} {2}"""

TEST_RESULT = """object_name: \033[1m{0}\033[0m
\u2799 test_func: \033[1m{1}\033[0m {2} \033[1m{3}\033[0m
"""


def create_fullwidth_line(input_string):
    try:
        available_columns = get_terminal_size().columns - len(input_string)
    except:
        available_columns = 80 - len(input_string)
    available_columns = 4 if available_columns < 4 else available_columns
    left_available_columns = available_columns // 2
    right_available_columns = available_columns // 2 + available_columns % 2
    return FULLWIDTH_LINE.format(
        "=" * (left_available_columns - 1),
        input_string,
        "=" * (right_available_columns - 1),
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
    terraform_data_path,
    total_tests,
):
    print(
        RUN_HEADER.format(
            create_fullwidth_line("tf2"),
            system_version().lower(),
            python_version(),
            package_version("tf2project"),
            terraform_version,
            format_version,
            loader_type,
            getcwd(),
            terraform_data_path,
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
    output_contents = []
    if total_failed_tests:
        output_contents.extend([str(total_failed_tests), "failed"])
    if total_passed_tests:
        output_contents.extend([str(total_passed_tests), "passed"])
    if not total_failed_tests and not total_passed_tests:
        output_contents.append("nothing")
    print(
        RUN_FOOTER.format(
            "\033[92m" if overall_result else "\033[91m",
            create_fullwidth_line(
                OUTPUT_STRING.format(
                    " ".join((output_contents)),
                    round(total_time, 2),
                ),
            ),
        )
    )
