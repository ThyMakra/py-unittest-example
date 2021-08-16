class AssistObjectB:
    @property
    def attribute(self):
        return "real attribute"

    # @property
    # def other_attribute(self):
    #     return "won't be accessed by the MockMagicmockDifference Object"


class MockObjectAttribute:
    def __init__(self, assist):
        self.assist = assist
    
    def get_assist_attribute(self):
        return self.assist.attribute