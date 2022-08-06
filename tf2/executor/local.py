# Terraform Test Framework
# https://github.com/tf2project/tf2project

from subprocess import TimeoutExpired
from subprocess import run as run_subprocess

from .executor import Executor


class LocalCommandExecutor(Executor):
    def execute(self, command, *args, **kwargs):
        try:
            result = run_subprocess(
                command,
                shell=True,
                capture_output=True,
                *args,
                **kwargs,
            )
        except TimeoutExpired as e:
            timeout = True
        except:
            pass
        finally:
            if "result" in locals():
                self._is_complete = True
                self._set_result(
                    command=command,
                    rc=result.returncode,
                    stdout=result.stdout.decode("utf8"),
                    complete=self._is_complete,
                )
            else:
                self._is_complete = False
                self._set_result(
                    command=command,
                    timeout=True if "timeout" in locals() else False,
                    complete=self._is_complete,
                )
