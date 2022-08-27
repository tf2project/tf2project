# Terraform Test Framework
# https://github.com/tf2project/tf2project

import pytest

from tf2 import Executor, LocalCommandExecutor


def test_local_command_executor():
    local_command_executor = LocalCommandExecutor()
    assert issubclass(LocalCommandExecutor, Executor) is True
    assert isinstance(local_command_executor, LocalCommandExecutor) is True
    assert isinstance(local_command_executor, Executor) is True
    local_command_executor.execute("true")
    assert local_command_executor.is_complete() is True
    assert local_command_executor.result.command == "true"
    assert local_command_executor.result.rc == 0
    assert local_command_executor.result.stdout == ""
    assert local_command_executor.result.complete is True
    local_command_executor.execute("false")
    assert local_command_executor.is_complete() is True
    assert local_command_executor.result.command == "false"
    assert local_command_executor.result.rc == 1
    assert local_command_executor.result.stdout == ""
    assert local_command_executor.result.complete is True
    local_command_executor.execute("sleep 10", timeout=1)
    assert local_command_executor.is_complete() is False
    assert local_command_executor.result.command == "sleep 10"
    assert local_command_executor.result.timeout is True
    assert local_command_executor.result.complete is False
    local_command_executor.execute("echo TF2Project", shell=False)
    assert local_command_executor.is_complete() is False
    assert local_command_executor.result.command == "echo TF2Project"
    assert local_command_executor.result.complete is False
