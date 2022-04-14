
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkUtil(root, level):
    # Base Case
    if root is None:
        return True
    # if a leaf node is encountered
    if root.left is None and root.right is None:
        if check.leafLevel == 0:
            check.leaflevel = level # Set first leaf found
            return True


        return level == check.leaflevel


    return (checkUtil(root.left, level+1) and
            checkUtil(root.right, level+1))


def check(root):
    level = 0
    check.leafLevel = 0
    return (checkUtil(root, level))


# Driver Code
if __name__ =="__main__":
    root = Node(12)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(9)
    root.left.left.left = Node(1)
    root.left.right.left = Node(2)

    if (check(root)):
        print('leaves are at same level')
    else:
        print("leaves are not at same level")

