import pytest

from src import misc


def test_misc_pass():
    """ 
    miscellanous test to print that the application is running
    """
    assert misc.health() == 'app is running...'