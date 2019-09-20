"""Operator class"""

import numbers


class Operator:
    """'Wrapper' for numpy operators"""

    def __init__(self, operator, strength):
        self.operator = operator
        self.strength = strength

    def execute(self, element1, element2, debug=True):
        """Use wrapped operator on two elements"""

        # Check type
        if not isinstance(element1, numbers.Number) or not isinstance(element2, numbers.Number):
            raise TypeError('Cannot execute operator if elements are not a number')
        result = self.operator(element1, element2)

        # Report
        if debug:
            print('Operator: ' + self.operator.__name__ +
                  '({:f}) {:f} =  {:f}'.format(element1, element2, result))

        return result
