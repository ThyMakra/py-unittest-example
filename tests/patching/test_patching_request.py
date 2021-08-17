from unittest import TestCase, mock
import requests
from requests.exceptions import ConnectionError

from src.patching.patching_request import requesting_github


def make_mock_json():
    return {
        'name': 'ThyMakra',
        'respository': 'py-unittest-example'
    }


def make_mock_response():
    response_mock = mock.Mock()
    # response_mock.json.return_value = make_mock_json()
    response_mock.json.side_effect = make_mock_json
    response_mock.status_code = 200
    return response_mock


class TestPatching(TestCase):
    # patch 
    @mock.patch('src.patching.patching_request.requests')
    def test_requesting_github(self, mock_requests):
        mock_requests.get.side_effect = [
            TimeoutError,
            make_mock_response()
        ]

        with self.assertRaises(TimeoutError):
            requesting_github()
            mock_requests.get.assert_called_once()

        response = make_mock_json()
        print(response)
        self.assertEqual(requesting_github(), response)

    # patching only an attribute of the dependency
    @mock.patch.object(requests, 'get', side_effect=[ConnectionError, TimeoutError])
    def test_requesting_github_exception(self, mock_requests):
        resp = requesting_github()
        # go to Exception part of the code
        self.assertEqual(resp, 'ConnectionError was raised')

        # Exception only raised in the test
        with self.assertRaises(TimeoutError):
            requesting_github()
