"""Queue, subclass of Container"""

from container.container import Container


class Queue(Container):
    """FIFO queue"""
    def __init__(self):
        """Initialization is done at superclass"""
        super().__init__()

    def peek(self):
        """Return the ∗first∗ element of the list, do not delete it"""
        assert not self.is_empty()
        return self._items[0]

    def pop(self):
        """Pop off the first element"""
        assert not self.is_empty()
        return self._items.pop(0)
