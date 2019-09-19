"""Function class"""

import numbers


class Function:
    """'Wrapper' for numpy functions"""

    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        """Use the wrapped function on an element"""

        # Check type
        if not isinstance(element, numbers.Number):
            raise TypeError('Cannot execute func if element is not a number')
        result = self.func(element)

        # Report
        if debug:
            print('Function: ' + self.func.__name__ + '({:f}) =  {:f}'.format(element, result))

        return result
