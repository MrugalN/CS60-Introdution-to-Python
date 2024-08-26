from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("CSTY50") == True
    assert is_valid("AB123") == True


def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_invalid_start():
    assert is_valid("123ABC") == False
    assert is_valid("A1B2C3") == False


def test_invalid_characters():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False


def test_invalid_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS50A") == False
    assert is_valid("CS100A") == False
