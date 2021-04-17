l = ['mango', 'mango', 'land', 'land']
s = set(l)
print(s)
l = list(set(l))
print(l)

dev = {'mango', 'land'}
qa = {'jack', 'land'}
all = dev | qa
assert len(all) == 3
assert all == {'mango', 'land', 'jack'}
print(all)

from dis import dis
dis('{1}')
print()
dis('set([1,2])')

fz = frozenset(range(10))
print(fz)

from unicodedata import name

names = {chr(i) for i in range(32,256) if 'SIGN' in name(chr(i), '')}
print(names)

dis('a = set([]);b = set([]);    c = set([]);    d = c.union(a, b);')
print()
dis('a = [];b = [];    c = set([]);    d = c.union(a, b);')

names.union()