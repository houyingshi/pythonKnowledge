from types import MappingProxyType

persons = {1:'mango', 2:'land'}
persons_proxy = MappingProxyType(persons)
print(persons_proxy)
assert persons_proxy[1] == persons[1]
assert len(persons_proxy) == len(persons)

try:
    persons_proxy[3] = 'jack'
except TypeError:
    print('we can not set item for mapping proxy type')

persons[3] = 'jack'
assert len(persons) == len(persons_proxy)
assert persons_proxy[3] == persons[3]