# Terraform Test Framework
# https://github.com/tf2project/tf2

from subprocess import TimeoutExpired
from subprocess import run as run_subprocess

from .executor import Executor, ExecutorResult


class LocalCommandExecutor(Executor):
    def __init__(self, command, *args, **kwargs):
        super().__init__()
        self._command = command
        self._args = args
        self._kwargs = kwargs
        self._execute()

    def _execute(self):
        try:
            self._command_result = run_subprocess(
                self._command,
                shell=True,
                capture_output=True,
                *self._args,
                **self._kwargs,
            )
        except TimeoutExpired as e:
            self._timeout = True
        except Exception as e:
            pass
        finally:
            if hasattr(self, "_command_result") is True:
                self._complete = True
                self.result = ExecutorResult(
                    rc=self._command_result.returncode,
                    stdout=self._command_result.stdout.decode("utf8"),
                    complete=self._complete,
                )
            else:
                self._complete = False
                self.result = ExecutorResult(
                    complete=self._complete,
                    timeout=True if hasattr(self, "_timeout") else False,
                )
