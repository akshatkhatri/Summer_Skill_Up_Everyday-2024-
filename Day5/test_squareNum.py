from SquaresAndStrings import square
from SquaresAndStrings import hello
import pytest

def test_square_positives():
    
    assert square(2) == 4
    assert square(3) == 9
    assert square(5) == 25

def test_square_negatives():
    assert square(-2) == 4
    assert square(-4) == 16
    assert square(-5) ==25

def test_square_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("Cat")

def test_str2():
    for name in ["Akshat","Ishita","Anshul"]:
        assert hello(name) == f"hello, {name}"

def test_default():
    assert hello() == f"hello, World"