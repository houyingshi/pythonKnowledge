from collections import UserDict

class StringKeyDict(UserDict):

    def __init__(self, items):
        super().__init__(items)
        # self.update(items)

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)

        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value

key_dict = StringKeyDict({1:'mango', '2':'land'})
print(key_dict[1])
print(key_dict['2'])
key_dict[3] = 'jack'
print(key_dict['3'])
assert 3 in key_dict
