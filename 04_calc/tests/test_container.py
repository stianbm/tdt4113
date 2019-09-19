"""Test for Container"""

from container.container import Container


def test_container():
    container = Container()
    item = 5
    item2 = 6

    assert container.is_empty()
    assert container.size() == 0

    container.push(item)
    assert container.size() == 1
    assert not container.is_empty()

    container.push(item2)
    assert container.size() == 2
    assert not container.is_empty()

    print('Container tested SUCCESSFULLY')
