"""Tests for Calculator"""
from numpy import exp

from calculator import Calculator
from container.queue import Queue
from function import Function
from operator_class import Operator


def test_calculator():

    # execute
    calc = Calculator()
    assert calc.functions['EXP'].execute(
        calc.operators['ADD'].execute(
            1, calc.operators['MULT'].execute(2, 3, False), False
        ), False
    ) == exp(7)

    # evaluate_rpn
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(calc.operators['MULT'])
    queue.push(calc.operators['ADD'])
    queue.push(calc.functions['EXP'])
    calc.output_queue = queue

    assert calc.evaluate_rpn(False) == exp(7)

    # shunting_yard
    print('SHUNT')
    input_queue = Queue()
    input_queue.push(calc.functions['EXP'])
    input_queue.push('(')
    input_queue.push(1)
    input_queue.push(calc.operators['ADD'])
    input_queue.push(2)
    input_queue.push(calc.operators['MULT'])
    input_queue.push(3)
    input_queue.push(')')

    print_container(calc.shunting_yard(input_queue))

    input_queue2 = Queue()
    input_queue2.push(2)
    input_queue2.push(calc.operators['MULT'])
    input_queue2.push(3)
    input_queue2.push(calc.operators['ADD'])
    input_queue2.push(1)

    print_container(calc.shunting_yard(input_queue2))

    # parser
    print('Parser')
    text = "EXP(1 ADD 2 MULT 3)"
    print_container(calc.parser(text))

    # calculate_expression
    print('CALCULATE ', text)
    result = calc.calculate_expression(text)
    print(result)
    assert result == exp(7)

    text = "((15 DIV (7 SUB (1 ADD 1))) MULT 3) SUB (2 ADD (1 ADD 1))"
    print('CALCULATE ', text)
    result = calc.calculate_expression(text)
    print(result)
    assert result == 5

    print('Calculator tested SUCCESSFULLY')


def print_container(container):
    """Iterates through containers and prints each element"""
    print()
    while not container.is_empty():
        element = container.pop()
        if isinstance(element, Operator):
            print(element.operator.__name__)
        elif isinstance(element, Function):
            print(element.func.__name__)
        else:
            print(element)
    print()
