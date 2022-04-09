# traversal in spiral form

class newNode:
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def height(node):

    if node == None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def printSpiral(root):
    h = height(root)

    ltr = height(root)
    itr = False
    for i in range(1, h+1):
        printGivenLevel(root, i, ltr)

        "Revert ltr to traverse next level in opposite order"
        ltr = not ltr

def printGivenLevel(root, level, ltr):

    if root == None:
        return
    if level == 1:
        print(root.data, end=' ')
    elif(level > 1):

        if ltr:
            printGivenLevel(root.left, level-1, ltr)
            printGivenLevel(root.right, level-1, ltr)
        else:
            printGivenLevel(root.right, level-1, ltr)
            printGivenLevel(root.left, level-1, ltr)




# driver code:
if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)
    print("spiral order traversal of binary tree is:")
    printSpiral(root)


# This method has a lot of recursion to be done
# Another iterative methods are present
