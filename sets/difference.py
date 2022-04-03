# Difference of the two sets

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)


set3 = set1.difference(set2)
print("Difference of the two sets "
      "using difference() function")
print(set3)

set3 = set1 - set2
print("\ndifference of the two sets using '-' operator")
print(set3)

set4 = set2 - set1
print(set4)

# Clearing of sets

set1 = {1, 2, 3, 4, 5, 6}
print("Initial set")
print(set1)

set1.clear()

print("\n Set after using clear() function ")
print(set1)

""""the downfall of is that the set does not maintain
 a particular order, only instances of immutable types
  can be added to a Python set"""
