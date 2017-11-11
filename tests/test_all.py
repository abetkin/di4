import sys

from pytest import fixture

@fixture(autouse=True)
def pythonpath():
    sys.path.append('..')
    yield


def test_1():
    from di4 import run

    class Ko1:
        def __init__(self):
            pass

    class Ko2:
        def __init__(self, ko1: Ko1):
            pass

    class Ko3:
        def __init__(self, ko2: Ko2):
            pass

    def func(ko2: Ko2):
        return isinstance(ko2, Ko2)
    
    assert run(func) is True
    assert isinstance(run(Ko3), Ko3)