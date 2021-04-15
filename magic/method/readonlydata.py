class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


p = Person('mongo')
print(p.name)
print(p.name())
