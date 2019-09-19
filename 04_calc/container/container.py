"""Container parent class"""


class Container:
    """Container parent class for Queue and Stack"""

    def __init__(self):
        self._items = []

    def size(self):
        """Return number of elements in self.items"""
        return len(self._items)

    def is_empty(self):
        """Check if self.items is empty"""
        # Pylint says not to use len() for this, StackOverflow says not to use alternative
        if len(self._items) == 0:
            return True
        return False

    def push(self, item):
        """Add item to end of self.items"""
        self._items.append(item)

    def pop(self):
        """Pop off the correct element of self.items , and return it
        This method differs between subclasses, hence is not implemented in the superclass"""
        raise NotImplementedError

    def peek(self):
        """Return the top element without removing it
        This method differs between subclasses, hence is not implemented in the superclass"""
        raise NotImplementedError
