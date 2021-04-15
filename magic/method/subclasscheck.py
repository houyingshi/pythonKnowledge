class MetaClass(type):
    def __subclasscheck__(self, subclass):
        if self == subclass.__base__:
            return True
        return False

class Base(metaclass=MetaClass):
    pass

class Sub(Base):
    pass

print(issubclass(int, Base))

print(issubclass(object, Base))

print(issubclass(Sub, Base))