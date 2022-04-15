class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to print reverse order traversal
def reverseLevelOrder(root):
    h = height(root)
    for i in reversed(range(1, h+1)):
        printGivenLevel(root, i)


# Print nodes at the given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")

    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

# height of the tree
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        #Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight+1


# Driver Program kto test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order traversal of binary tree is :")
reverseLevelOrder(root)
