people = {'jay', 'idrish', ' archana'}
print(f"people: {people}", end=" ")

people.add('dinesh')
print(f"people: {people}", end=" ")

for i in range(1, 6):
    people.add(i)

print("\n Set after elements: ", end=" ")
print(people)
