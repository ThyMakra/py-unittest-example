class MockReturnvalue:
    def __init__(self, assist):
        self.assist = assist

    def get_assist_attribute(self):
        return self.assist.get_attribute()


class MockSideeffect:
    def some_func():
        return "a value to return that will never be returned"

 
def get_the_mock_side_effect(mock_side_effect):
    try:
        return mock_side_effect.some_func()
    except ValueError:
        return 'ValueError was raised'
