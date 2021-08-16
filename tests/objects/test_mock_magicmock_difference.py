from unittest import mock

from src.objects.mockMagicmockDifference import MockMagicmockDifference


def test_mock_magicmock_difference():
    assist = mock.Mock()

    difference = MockMagicmockDifference(assist)

    ## to fail and see the difference between Mock() and MagicMock()
    # assert difference.get_assist_attribute() == assist.attribute()

    """ Mock
    AssertionError: assert 
        <Mock name='mock.attribute' id='4386323088'> == <Mock name='mock.attribute()' id='4386323328'>
    where 
        <Mock name='mock.attribute' id='4386323088'> = <bound method UrlObject.get_assist_attribute of <src.objects.url.UrlObject object at 0x10571f970>>()
    
    """    
    
    """ Magic Mock
    AssertionError: assert 
        <MagicMock na...='4388616800'> == <MagicMock na...='4388512576'>
    """ 

    # pass
    assert difference.get_assist_attribute() == assist.attribute
    