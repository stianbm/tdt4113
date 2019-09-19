"""Stack, subclass of Container"""

from container.container import Container


class Stack(Container):
    """FILO stack"""
    def __init__(self):
        super().__init__()

    def peek(self):
        """Return the last element of the list"""
        assert not self.is_empty()
        return self._items[-1]

    def pop(self):
        """Pop off the last element"""
        assert not self.is_empty()
        return self._items.pop(-1)
