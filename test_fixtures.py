import pytest


@pytest.fixture()
def port() -> int:
    return 25


def test_mail_connection(port: int):
    assert port == 8080
