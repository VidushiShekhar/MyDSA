" Method 1: Simple is to construct a tree from the given inorder and preorder traversal"
" Method 2: without constructing the tree .root is first in preorder"
" and last in post order first left,"
" then right then root, recursively"


# utility function to search x in arr[] of size n
def search(arr, x, n):
    for i in range(n):
        if arr[i] == x:
            return i

    return -1

# prints postorder traversal from
def printPostOrder(In, pre, n):
    root = search(In, pre[0], n)

    if root != 0:
        printPostOrder(In[0:root], pre[1:n], root)

    if root != n-1:
        printPostOrder(In[root+1:n], pre[root+1:n], n-root-1)


    print(pre[0], end=" ")

# Driver code
In = [4, 2, 5, 1, 3, 6]
pre = [1, 2, 4, 5, 3, 6]
n = len(In)
print("Postorder traversal ")

printPostOrder(In, pre, n)