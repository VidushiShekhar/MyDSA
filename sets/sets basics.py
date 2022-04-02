"""A set is an unordered collection data type that is iterable,
mutable and has no duplicate elements"""

# python program to demonstrate sets
# Same as {"a", "b", "c"}
myset = set(["a", "b", "c"])
print(myset)

myset.add('d')
print(myset)

""" Frozen Sets in python are immutable objects """


normal_set = set(["a", "b", " c"])
print(normal_set)
# A frozen Set
frozen_set = frozenset(["e", "f", "g"])
print()

