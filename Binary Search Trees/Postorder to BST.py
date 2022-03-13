# Class of Root Node:

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A function to construct a binary search tree from the postorder array given:


def constructTree(post, start, end):


    # base case:
    if start > end:
        return None
    # begin search from the end and find the smallest element in the array
    node = Node(post[end])
    end -= 1
    i = end
    while i >= start:
        if post[i] < post[end]:
            break
        i -= 1
    # to define the right and left of the node selected:
    node.right = constructTree(post, i+1, end)
    node.left = constructTree(post, start, i)
    return node


# recure on both the side left and right
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


post = [1, 7, 5, 50, 40, 10]
# Driver code
root = constructTree(post, 0, len(post)-1)
printInorder(root)