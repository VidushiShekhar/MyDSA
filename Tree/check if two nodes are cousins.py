class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSibling(root, a, b):

    # Base Case
    if root is None:
        return 0
    return ((root.left == a and root.right == b) or
            (root.left == b and root.right == a) or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b))

# recursive function to find level of Node
def level(root, ptr, lev):
    if root is None:
        return 0
    if root == ptr:
        return lev

    l = level(root.right, ptr, lev+1)

    if l!= 0:
        return l
    return level(root.right, ptr, lev +1)


# return 1  if a and b are cousins else zero
def iscousin(root, a, b):
    if ((level(root, a, 1) == level(root, b, 1))and
            not (isSibling(root, a, b))):
        return 1
    else:
        return 0






# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

node1 = root.left.right
node2 = root.right.right

print("Yes" if iscousin(root, node1, node2) == 1 else "No")