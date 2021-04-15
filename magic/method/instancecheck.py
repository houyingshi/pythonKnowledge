print(isinstance(123, int))

class MyMetaClass(type):
    def __instancecheck__(self, instance):
        if self.__qualname__ == type(instance).__qualname__:
            return True

        return False

class MyClass(metaclass=MyMetaClass):
    pass

class dirty:
    pass

print(isinstance(123, MyClass))

obj = dirty()
print(isinstance(obj, MyClass))
print(isinstance(MyClass(), MyClass))

