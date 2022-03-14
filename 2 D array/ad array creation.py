# 1 D array creation
N = 5
arr = [0]*N
print(arr)

# Method 2:
N = 5
arr = [0 for i in range(N)]
print(arr)

# 2D array creation
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)



rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

rows, cols =5, 5
arr = []
for i in range(rows):
    col =[]
    for j in range(cols):
        col.append(0)
    arr.append(col)
print(arr)


rows, cols = (5, 5)
arr = [[0]*cols]*rows
arr[0][0] = 1

for row in arr:
    print(row)
print('\n')


# 2B
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0] = 1
for row in arr:
    print(row)
# both the technique have a different method the object are assigned differently
# better way to declare 2D array:
rows, cols = (3, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
"""Hence the better way to declare a 2d array is 
"""
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
# the above method create separate list
""" using is operator to check for the same object"""

arr =[[0 for i in range(cols)] for j in range(rows)]
# check if arr[0] and arr[1] refer to same object
print(arr[0] is arr[1])
arr[1][0] = 1
print(arr[0][0] is arr[1][0])

# method 2a

arr = [[0]*cols]*rows

print(arr[0] is arr[1])
# the above function print True



