class Field:
    def __init__(self, default=sentinel):
        self.value = default

    def set(self, value):
        self.value = value

    def get(self):
        if self.value is sentinel:
            raise ValueError("this field has no value!")

