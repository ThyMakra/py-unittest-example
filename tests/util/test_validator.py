import pytest

from src.util.validator import validate_url


def test_validate_url():
    url = 'http://github.com/ThyMakra'

    # pass
    assert validate_url('http://github.com/ThyMakra') == url
    assert validate_url('github.com/ThyMakra') == url

    # raising exception
    with pytest.raises(ValueError):
        # this statement will fail if the code does not raise an exception
        validate_url('http:///path')
        # validate_url('http://a/path')
    with pytest.raises(ValueError, match="^Invalid URL scheme: .*"):
        validate_url('ssh:///test@test.example:22')
        # validate_url('http:///test@test.example')
