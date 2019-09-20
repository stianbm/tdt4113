"""Tests for Function"""

from function import Function
from numpy import exp, sin


def test_function():
    exponential_func = Function(exp)
    sin_func = Function(sin)
    # print(exponential_func.execute(sin_func.execute(0)))

    assert sin_func.execute(0, False) == 0
    assert exponential_func.execute(sin_func.execute(0, False), False) == 1

    print('Function tested SUCCESSFULLY')
