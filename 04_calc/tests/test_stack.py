"""Tests for Stack"""

from container.stack import Stack


def test_stack():
    stack = Stack()
    item = 5
    item2 = 6

    stack.push(item)
    assert stack.peek() == item

    stack.push(item2)
    assert stack.peek() == item2

    assert stack.pop() == item2
    assert stack.pop() == item

    print('Stack tested SUCCESSFULLY')
