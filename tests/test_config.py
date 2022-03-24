import pytest


def test_generic():
    a = 30
    b = 40
    assert a != b

def test_mul():
    a = 30
    b = 40
    c = a*b
    assert c >= 100


class NotInRange(Exception):
    def ___init__(self, message="value not in range"):
        # self.input_ = input_
        self.message = message
        super().__init__(self.message)


def test_generic1():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange
        
