class AssistObjectB:
    @property
    def attribute(self):
        return "real attribute"


class MockObjectAttribute:
    def __init__(self, assist):
        self.assist = assist
    
    def get_assist_attribute(self):
        return self.assist.attribute


def set_attribute_of_mock(temp):
    temp.attribute_to_be_set = 'youre no longer a mock now'