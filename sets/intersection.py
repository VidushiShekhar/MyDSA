# Intersection of the sets

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)

# Intersection using Intersection() function

set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using & operator
set4 = set1 & set2
print("\n Intersection using & operator: ")
print(set3)

"""Set differ from lists and tuples 
as it cannot have multiple occurence
 of the same element and store unordered values """

