from twttr import shorten


def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("apple") == "ppl"
    assert shorten("hello") == "hll"


def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("APPLE") == "PPL"
    assert shorten("HELLO") == "HLL"


# def test_shorten_mixed_case():
#     assert shorten("TwItTeR") == "TwtTR"
#     assert shorten("ApPlE") == "ppl"
#     assert shorten("HeLLo") == "HLL"


def test_shorten_with_numbers():
    assert shorten("123") == "123"
    assert shorten("twi77er") == "tw77r"


def test_shorten_with_special_characters():
    assert shorten("t@w!t#t$r") == "t@w!t#t$r"
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"
