from some_module import add_stuff
import pytest


# Basic test functions are fun
def test_assertion_example():
    assert 1 == 1


def test_expected_error_example():
    with pytest.raises(AssertionError):
        assert 1 == 2


# Example class based testing. Useful if you have some data
# to generate first which you can store as a class variable
# instead of regenerating it for each function
class TestClass(object):
    def __init__(self):
        self.something = 1

    def test_add_stuff(self):
        assert add_stuff(1, 2) == 3
