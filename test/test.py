import pytest
from functions import square
from functions import hello_name


def test_hello_name_input():
    assert hello_name("John") == "Hello, John"

def test_hello_name_default():
    assert hello_name() == "Hello, World"

def test_positive():  
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")