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
