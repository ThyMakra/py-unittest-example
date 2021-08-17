import unittest
import pytest
import datetime
from unittest import TestCase, mock

from src.patching.patching_datetime import create_data, is_weekday


class TestPatching(TestCase):
    # @pytest.fixture
    # def add_data(self, patch):
    #     return patch('src.patching.create_data.add_data')

    @mock.patch('src.patching.patching_datetime.add_data')
    def test_create_data(self, mocked_add_data):
        mocked_add_data.return_value = 'some other mocked response'
        response = create_data()
        self.assertEqual(response, 'some other mocked response')

    @mock.patch('src.patching.patching_datetime.datetime')
    def test_is_weekday(self, mocked_datetime):
        tuesday = datetime.datetime(year=2019, month=1, day=1)
        saturday = datetime.datetime(year=2019, month=1, day=5)

        mocked_datetime.datetime.today.return_value = tuesday
        assert is_weekday()

        mocked_datetime.datetime.today.return_value = saturday
        assert not is_weekday()
