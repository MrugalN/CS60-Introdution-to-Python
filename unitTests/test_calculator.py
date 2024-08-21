# assert - Use to test the correctness of a program
# pytest - A testing framework that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

from calculator import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
