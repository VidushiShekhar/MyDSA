
# Find the sum of Covered and uncovered nodes of binary tree
class newNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


# find the sum of all the roots
def Sum(t):
    if t == None:
        return 0
    return t.key + Sum(t.left) + Sum(t.right)

def uncoveredSumleft(t):
    if t.left ==None and t.right ==None:
        return t.key
    if t.left != None:
        return t.key + uncoveredSumleft(t.left)
    else:
        return t.key + uncoveredSumleft(t.right)

# Recursive function to calculate sum of right boundary elements
def uncoveredSumright(t):

    if t.left == None and t.right == None:
        return t.key

    if t.right !=None:
        return t.key + uncoveredSumright(t.right)
    else:
        return t.key + uncoveredSumright(t.left)


# Return sum of uncovered elements
def uncoverSum(t):

    # Initializing with 0 in case we don't have a left or right boundary
    lb = 0
    rb = 0

    if t.left != None:
        lb = uncoveredSumleft(t.left)
    if t.right != None:
        rb = uncoveredSumright(t.right)

    return t.key + lb + rb

def isSumSame(root):
    sumUC = uncoverSum(root)
    sumT = Sum(root)


# utility to print inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Driver Code
if __name__ == "__main__":

    root = newNode(8)
    root.left = newNode(3)

    root.left.left = newNode(1)
    root.left.right = newNode(6)
    root.left.right.left = newNode(4)
    root.left.right.right = newNode(7)

    root.right = newNode(10)
    root.right.right = newNode(14)
    root.right.right.left = newNode(13)

    if isSumSame(root):
        print("Sum of covered and uncovered is same")
    else:
        print("Sum of covered and uncovered is not the same")

