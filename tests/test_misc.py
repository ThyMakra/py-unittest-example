from src import misc


def test_misc():
    """ 
    miscellanous test to print that the application is running
    """
    assert misc.health() == 'app is running...'
    