from unittest import mock

from src.objects.mock_object_attribute import MockObjectAttribute, set_attribute_of_mock


def test_mock_object_attribute():
    assist = mock.Mock()
    assist.attribute = 'this is a mocked attribute'

    mock_attribute = MockObjectAttribute(assist)
    assert mock_attribute.get_assist_attribute() == 'this is a mocked attribute'


def test_set_attribute_of_mock():
    mock_object = mock.Mock()

    set_attribute_of_mock(mock_object)

    assert mock_object.attribute_to_be_set == 'youre no longer a mock now'
    