# Testing hello_name code

from functions import hello_name

def test_hello_name_input():
    assert hello_name("John") == "Hello, John"
def test_hello_name_default():
    assert hello_name() == "Hello, World"

# see test subdirectory readme for more