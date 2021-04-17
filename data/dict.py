persons = {1:'mango', 2:'land'}
for p in persons:
    print(p)

persons = {2:'land', 1:'mango'}
for p in persons:
    print(p)

for p in persons.items():
    print(p)

class StringKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()

strDict = StringKeyDict()
strDict['1'] = 'mango'
strDict['2'] = 'land'

assert strDict['1'] == 'mango'
assert strDict[2] == 'land'
assert 1 in strDict

from collections import OrderedDict, ChainMap

od = OrderedDict()
od['name'] = 1
od['age'] = 2
od['girl'] = 3
od['money'] = 4
od['hourse'] = None
for item in od.items():
    print(item)

d = dict()
d['name'] = 1
d['age'] = 2
d['girl'] = 3
d['money'] = 4
d['hourse'] = None
print()
for item in od.items():
    print(item)

od = OrderedDict().fromkeys('abcde')
od.move_to_end('b')
print(''.join(od.keys()))

# ChinaMap
import os, argparse
defaults = {'color':'red', 'user':'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
user_args = parser.parse_args()

user_args_dict = {k:v for k,v in vars(user_args).items() if v is not None}

combined = ChainMap(user_args_dict, os.environ, defaults)
print(combined['color'])
print(combined['user'])
