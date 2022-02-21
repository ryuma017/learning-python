# __metaclass__ = type

class Person:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print(f"こんにちは、私は{self.name}です")