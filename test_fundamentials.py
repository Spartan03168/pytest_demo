"""This module contains basic tests.

Broke each of them and check how pytest shows an error.
You can run single test with -k option, e.g.:
pytest -k equality_strings
This will run only tests contain equality_strings in the name.
"""


def test_equality_strings():
    assert 'foobar' == 'fobar'
    # Broken

def test_equality_close_text():
    # Change 1 symbol inside string
    assert 'Intro to Programming 3: Python' == 'Intro to Programming 3:  Python'
    # Broken

def test_equality_with_long_text():
    source = '1' * 100 * '2' * 100 #100 * '2' broke this test.
    with_a = source  # .replace('12', 'a')
    with_b = source  # .replace('12', 'b')
    assert with_a == with_b
    # Broken

def test_equality_list():
    assert [0, 1, 3, 420] == [0, 1, 3, 69]
    # Broken

def test_equality_dict():
    assert {'banana': 1, 'cherry': 4, 'Kiwi': 1} == {'banana': 1, 'cherry': 4, 'apple': 13}
    # Broken


def test_equality_set():
    assert {'banana', 'cherry', 'orange'} == {'banana', 'cherry', 'banana'}
    # Broken

def test_equality_list_different_length():
    assert list('12345') == ['1', '2', '3', '4']
    # Broken

def test_in():
    assert 'Space' in 'Harbour.space'
    # Broken
