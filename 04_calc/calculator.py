"""Calculator class"""

import numbers
import re

from numpy import exp, log, sin, cos, sqrt, add, multiply, divide, subtract

from container.queue import Queue
from container.stack import Stack
from function import Function
from operator_class import Operator


class Calculator:
    """Binds Functions and Operators and have translating methods"""

    def __init__(self):
        # Define the functions supported by linking them to Python
        # functions. These can be made elsewhere in the program,
        # or imported (e.g. from numpy)
        self.functions = {'EXP': Function(exp),
                          'LOG': Function(log),
                          'SIN': Function(sin),
                          'COS': Function(cos),
                          'SQRT': Function(sqrt)}

        # Define the operators supported.
        # Link them to Python operators (here: from numpy)
        self.operators = {'ADD': Operator(add, 0),
                          'MULT': Operator(multiply, 1),
                          'DIV': Operator(divide, 1),
                          'SUB': Operator(subtract, 0)}

        # Define the output-queue. The parse_text method fill this with RPN.
        # Te evaluate_output_queue method evaluates it
        self.output_queue = Queue()

    def evaluate_rpn(self, debug=True):
        """Iterate through the output_queue and evaluate the content"""
        stack = Stack()
        while not self.output_queue.is_empty():
            element = self.output_queue.pop()

            if isinstance(element, numbers.Number):
                stack.push(element)

            elif isinstance(element, Function):
                stack_element = stack.pop()
                result = element.execute(stack_element, debug)
                stack.push(result)

            elif isinstance(element, Operator):
                stack_element1 = stack.pop()
                stack_element2 = stack.pop()
                result = element.execute(stack_element1, stack_element2, debug)
                stack.push(result)

            else:
                raise Exception(
                    'Stack element {} was not recognized'.format(element))

        return stack.pop()

    @staticmethod
    def shunting_yard(input_queue):
        """Implements shunting-yard algorithm for parsing text queue to RPN"""

        operator_stack = Stack()
        output_queue = Queue()

        while not input_queue.is_empty():
            element = input_queue.pop()

            if isinstance(element, numbers.Number):
                output_queue.push(element)

            elif isinstance(element, Function):
                operator_stack.push(element)

            elif element == '(':
                operator_stack.push(element)

            elif element == ')':
                while operator_stack.peek() != '(':
                    output_queue.push(operator_stack.pop())
                operator_stack.pop()

            elif isinstance(element, Operator):
                while not operator_stack.is_empty() and (isinstance(
                    operator_stack.peek(), Function) or (
                    isinstance(
                        operator_stack.peek(), Operator) and (
                        operator_stack.peek().strength >= element.strength))):
                    output_queue.push(operator_stack.pop())
                operator_stack.push(element)

        while not operator_stack.is_empty():
            output_queue.push(operator_stack.pop())

        return output_queue

    def parser(self, text):
        """Takes a text and returns it as a list of keywords for shunting_yard"""
        text = text.upper()
        text = re.split('([^A-Z0-9])', text)

        output_queue = Queue()
        for element in text:

            if element.isdigit():
                output_queue.push(float(element))

            elif element == ' ':
                pass

            elif element in self.functions.keys():
                output_queue.push(self.functions[element])

            elif element in self.operators.keys():
                output_queue.push(self.operators[element])

            else:
                output_queue.push(element)

        return output_queue

    def calculate_expression(self, text):
        """Runs text through parser, shunting yard, updates local queue with result,
        then runs evaluate_rpn"""

        parsed_text = self.parser(text)
        rpn_text = self.shunting_yard(parsed_text)

        self.output_queue = rpn_text

        return self.evaluate_rpn(False)
