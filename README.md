# Python Unit Testing

Some examples of Python Unit testing.

- Using Makefile

    ```bash
    make test
    ```

    > Running the tests is not the goal of this project, but the information and the examples of different topics regarding `Unit Testing`

## Topics

1. [Raising exception with `pytest`](tests/util/test_validator.py)
2. Mock and MagicMock
    1. [Difference of Mock() and MagicMock(). Difference in error raised](tests/objects/test_mock_magicmock_difference.py#L14)
    2. [Mocking an object attribute](tests/objects/test_mock_object_attribute.py#L11) or [Set a value to a mock's attribute](tests/objects/test_mock_object_attribute.py#L19)
    3. [Return value and Side effect](tests/functions/test_mock_callback.py#L10)
3. Patch (TODO)
4. Sentinel (TODO)
## Reference

1. Blog | Python Unit tests at Hypothesis : https://www.seanh.cc/2017/01/15/python-unit-tests-at-hypothesis/
