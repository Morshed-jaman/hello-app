from logic import greet


def test_greet_name():
    assert greet("Rahim") == "Hello Rahim"


def test_greet_empty():
    assert greet("") == "Hello "

