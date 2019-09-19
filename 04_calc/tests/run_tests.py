"""Runs tests"""

from tests.test_container import test_container
from tests.test_queue import test_queue
from tests.test_stack import test_stack


def main():
    """Run tests"""
    test_container()
    test_queue()
    test_stack()


if __name__ == "__main__":
    main()
