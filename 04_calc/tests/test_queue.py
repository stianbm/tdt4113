"""Tests for Queue"""

from container.queue import Queue


def test_queue():
    queue = Queue()
    item = 5
    item2 = 6

    queue.push(item)
    assert queue.peek() == item

    queue.push(item2)
    assert queue.peek() == item

    assert queue.pop() == item
    assert queue.pop() == item2

    print('Queue tested SUCCESSFULLY')
