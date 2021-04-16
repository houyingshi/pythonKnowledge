lax_coordinates = (33, -118)
latitude, longitude = lax_coordinates
print(latitude, longitude)

city, year, pop, chg, area = ('tokyo', 2021, 32450, 0.66, 8017)
traveler_ids = [{'usa', '3321'}, {'bra', 'CE3424567'}, {'esp', 'xda205856'}]

for passport in traveler_ids:
    print('%s' %passport)
    print(passport)


for country, _ in traveler_ids:
    print(country)


# 交换变量的值
a = 1
b = 2
a,b = b, a
assert a == 2
assert b == 1

# 元组作为函数参数自动拆包
result = divmod(20, 8)
assert result == (2, 4)
t = (20, 8)
result = divmod(*t)  #unpacking
assert result == (2, 4)
quotient, remainder = divmod(*t)
assert quotient == 2
assert remainder == 4

import os
path,name = os.path.split('/home/mango/tuple.py')
assert name == 'tuple.py'


a, b, *rest = range(1, 5)
assert a == 1
assert b == 2
print(rest)
assert rest == [3, 4]

a, b, *rest = range(1, 4)
assert a == 1
assert b == 2
assert rest == [3]

a, b, *rest = range(1, 3)
assert a == 1
assert b == 2
assert rest == []

*rest, a, b = range(1, 5)
assert rest == [1, 2]
assert a == 3
assert b == 4