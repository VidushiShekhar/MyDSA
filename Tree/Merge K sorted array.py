def mergeKArrays(arr, a, k):
    c = 0
    # traverse the matrix
    output = [0 for i in range(a*k)]
    for i in range(a):
        for j in range(k):
            output[c] = arr[i][j]
            c += 1
    # sort the array
    output.sort()
    return output

def printArray( arr, size):
    for i in range(size):
        print(arr[i], end= " ")

if __name__ == '__main__':
    arr = [[2, 6, 21, 34], [1, 3, 26, 100], [23, 34, 98, 200],[3,6,90,123]]
    k = 4
    n = 4

    sorted = mergeKArrays(arr, n, k)

    print("Merged array is ")
    printArray(sorted, n * k)


