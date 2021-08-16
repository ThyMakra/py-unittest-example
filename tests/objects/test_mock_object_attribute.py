from unittest import TestCase, mock
import unittest

from src.objects.mock_object_attribute import MockObjectAttribute, set_attribute_of_mock


class TestMockObject(TestCase):
    def test_mock_object_attribute(self):
        assist = mock.Mock()
        assist.attribute = 'this is a mocked attribute'

        mock_attribute = MockObjectAttribute(assist)
        assert mock_attribute.get_assist_attribute() == 'this is a mocked attribute'


    def test_set_attribute_of_mock(self):
        mock_object = mock.Mock()

        set_attribute_of_mock(mock_object)

        assert mock_object.attribute_to_be_set == 'youre no longer a mock now'
        
        # set attribute from the test
        mock_object = mock.Mock(a='a')
        assert mock_object.a == 'a'
        # mock will not raise AttributeError but it will just create a new mock object in itself
        self.assertIsInstance(mock_object.attribute_just_added, mock.Mock)