from unittest import mock

from src.objects.mock_magicmock_difference import MockMagicmockDifference


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
    """ 
    The test passes because the first time our mock assist’s assist.attribute is accessed 
    (by the MockMagicmockDifference.get_assist_attribute() code when the test calls it) 
    it returns the same other mock object as the second time it’s accessed 
    (by the assert statement in the test itself). 
    
    The assert statement relies on this property of mocks to pass. 
    If MockMagicmockDifference had used some other attribute of the mock annotation, 
    say assist.other_attribute instead of assist.attribute,
    that would have returned a different other mock object and the assert would have failed.
    """
    # assert difference.get_assist_attribute() == assist.other_attribute