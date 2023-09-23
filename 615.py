# test to see if the square function works

from functions import square


def main():
    test_square()


def test_square():
    try:    
        assert square(2) == 4
        assert square(3) == 9
    except AssertionError:
        print("AssertionError")

if __name__ == "__main__":
    main()
    