# Multidimensional list in python:

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
print(a)
a = [[2, 4, 6, 8], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
for record in a:
    print(record)

# Accessing Using square rackets:
a = [[2, 4, 6, 8], [1, 3, 5, 7], [8, 6, 4, 2], [7, 5, 3, 1]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='')
    print()

# Create a list with All zeros:

m = 4
n = 5
a =[[0 for i in range(n)] for j in range(m)]
print(a)
# Methods on multidimensional lists:

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a.append([5, 10, 15, 20])
print(a)
a[3].append(14)
print(a)
# extent add the elements of the list(or any iterable) to the end of the current list

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[0].extend([12, 14, 16, 18])
print(a)
a.extend([[12, 14, 16, 18]]) # test the result for a.extend([12,14, 16,18])
print(a)

# reverse the sublist
a = [[2, 4, 6, 8, 10, 12, 14, 16, 18], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
# a[2].reverse()
# print(a)
# reverse the order of all the list:
for i in range(len(a)):
    a[i].reverse()
print(a)

