# 16012019
# Python's general purpose built-in containers: dict, list, set, tuple
# https://dbader.org/blog/writing-clean-python-with-namedtuples

from collections import defaultdict, namedtuple, Counter, deque

# tuples are immutable
# tuples can hold more than 2 elements
# data can be accessed only by using indexes
classic_tuple = ('ford', 'mondeo', 'hatchback')

print(f'{classic_tuple[0]} {classic_tuple[1]} {classic_tuple[2]}')


Car = namedtuple('Car', 'make model')

print(hex(id(Car)))
# why class is 'type'?
print(type(Car))

car1 = Car(make='ford', model='mondeo')
car2 = Car(make='dacia', model='lodgy')
car3 = car1

print(id(car1))
print(id(car3))

print(type(car1))

print(car1.make)
print(car1.model)
print(car2.make)
print(car2.model)

