"""Tests for Operator"""

from operator_class import Operator
from numpy import add, multiply


def test_operator():

    add_operator = Operator(add, strength=0)
    multiply_operator = Operator(multiply, strength=1)

    assert add_operator.execute(1, multiply_operator.execute(2, 3, False), False) == 7

    print('Operator tested SUCCESSFULLY')
