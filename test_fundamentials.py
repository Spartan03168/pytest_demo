"""This module contains basic tests.

Broke each of them and check how pytest shows an error.
You can run single test with -k option, e.g.:
pytest -k equality_strings
This will run only tests contain equality_strings in the name.
"""


def test_equality_strings():
    assert 'foobar' == 'foobar'


def test_equality_close_text():
    # Change 1 symbol inside string
    assert 'Intro to Programming 3: Python' == 'Intro to Programming 3: Python'


def test_equality_with_long_text():
    source = '1' * 100 + '2' * 100
    with_a = source  # .replace('12', 'a')
    with_b = source  # .replace('12', 'b')
    assert with_a == with_b


def test_equality_list():
    assert [0, 1, 3] == [0, 1, 3]


def test_equality_dict():
    assert {'banana': 1, 'cherry': 4} == {'banana': 1, 'cherry': 4}


def test_equality_set():
    assert {'banana', 'cherry'} == {'banana', 'cherry', 'banana'}


def test_equality_list_different_length():
    assert list('1234') == ['1', '2', '3', '4']


def test_in():
    assert 'Space' in 'Harbour.Space'
