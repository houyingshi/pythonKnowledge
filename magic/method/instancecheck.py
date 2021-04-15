print(isinstance(123, int))

class MyMetaClass(type):
    def __instancecheck__(self, instance):
        if hasattr(instance, 'instance_check_test'):
            return True

        return False

class MyClass(metaclass=MyMetaClass):
    pass

class dirty:
    pass

print(isinstance(123, MyClass))

obj = dirty()
print(isinstance(obj, MyClass))
obj.instance_check_test = True
print(isinstance(obj, MyClass))

print(issubclass(type(obj), MyClass))