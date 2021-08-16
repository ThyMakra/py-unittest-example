from unittest import TestCase, mock

from src.functions.mock_callback import MockReturnvalue, get_the_mock_side_effect


def make_new_side_effect_function():
    return 'output of the replaced function'


class TestMockCallback(TestCase):
    def test_mock_return_value(self):
        my_mock = mock.Mock()
        my_mock.return_value = 'return value of mock'
        # mock can be called
        self.assertEqual(my_mock(), 'return value of mock')
        
        my_mock.new_attribute.return_value = 'return value of mock\'s new attribute'
        # set return value of a mock's attribute 
        self.assertEqual(my_mock.new_attribute(), 'return value of mock\'s new attribute')

        """ Make the class use the mock's defined attribute """
        assist_mock = mock.Mock()
        assist_mock.get_attribute.return_value = 'called get_attribute of assist'

        value_returned = MockReturnvalue(assist_mock).get_assist_attribute()
        self.assertEqual(value_returned, 'called get_attribute of assist')

    def test_mock_side_effect(self):
        mock_side_effect = mock.Mock()
        mock_side_effect.some_func.side_effect = [
            ValueError,
            'replace some func return value',
        ]
        
        # 1st side effect
        effect_1 = get_the_mock_side_effect(mock_side_effect)
        # raise an exception that will be handled by the calling function
        self.assertEqual(effect_1, 'ValueError was raised')

        # 2nd side effect
        effect_2 = get_the_mock_side_effect(mock_side_effect)
        self.assertEqual(effect_2, 'replace some func return value')

        # replace side effect with a whole new function
        mock_side_effect.some_func.side_effect = make_new_side_effect_function
        new_effect = get_the_mock_side_effect(mock_side_effect)
        self.assertEqual(new_effect, 'output of the replaced function')
