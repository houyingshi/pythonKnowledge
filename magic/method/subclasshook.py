from abc import ABCMeta



class Base(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, C):
        print(type(C))
        if C is Base:
            return type(C).__dict__.has_key('__greet__')
            # return (C, "__greet__")
        return False

    def __greet__(self):
        pass

class Sub(Base):
    def __greet__(self):
        pass

print(isinstance(object(), Base))
print(isinstance(Sub(), Base))

