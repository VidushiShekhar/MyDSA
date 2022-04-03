people = {'aman', 'jay', 'arjun'}
vampires = {" karan", 'kabir'}
angles = {"fairy", "sona"}
population = people.union(vampires)
print("Union using union() function")
print(population)

# using | operator we can have union
population = people | angles
print("\n Union using | operator")
print(population)


