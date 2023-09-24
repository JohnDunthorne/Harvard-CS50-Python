# use pytest to test square function
# remember ***pip install pytest***
# in the command line
# docs.pytest.org for documentation
from functions import square

def test_positive():  
    assert square(2) == 4
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

# to test this with pytest
# write
# pytest 627.py
# in the command line
# so pytest followed by the file name