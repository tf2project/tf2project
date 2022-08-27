# Terraform Test Framework
# https://github.com/tf2project/tf2project

import pytest

from tf2 import Executor


def test_executor():
    executor = Executor()
    assert hasattr(executor, "_is_executor") is True
    assert hasattr(executor, "_is_complete") is True
    assert hasattr(executor, "is_executor") is True
    assert hasattr(executor, "is_complete") is True
    assert hasattr(executor, "_set_result") is True
    assert hasattr(executor, "execute") is True
    assert hasattr(executor, "result") is True
    assert executor.result is None
    assert executor.is_executor() is True
    assert executor.is_complete() is False
    executor._set_result(earth="test", moon="test")
    assert isinstance(executor.result, Executor.Result)
    assert hasattr(executor.result, "earth") is True
    assert hasattr(executor.result, "moon") is True
    assert executor.result.earth == "test"
    assert executor.result.moon == "test"
    with pytest.raises(Exception) as e:
        executor.execute()
        assert e == "Method is not implemented."
