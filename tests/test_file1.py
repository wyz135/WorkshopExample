from some_module.file1 import add_stuff


def test_add_basic():
    assert add_stuff(1, 2) == 3
