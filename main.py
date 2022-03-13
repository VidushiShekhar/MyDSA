class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#create root
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.right = Node(4)

#Tree Traversals(Inorder, Preorder and Postorder)

def printInorder(root):

    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recure on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val)




# A function to do preorder tree traversal


def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)
# Driver Code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print('Preorder:')
printPreorder(root)

print('Inorder:')
printInorder(root)

print('Postorder:')
printPostorder(root)

# Inorder Traversal without recursion