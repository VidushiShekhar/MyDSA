#python3 program to check if two nodes in binary treeare cousins

# A binary Tree Node
class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

# Returns True if a and b
# are cousins otherwise False
def isCousin(root, a, b):
    if root == None:
        return False
    # To store parent of node a
    parA = None

    # To store parent of node b
    parB = None

    q = []

    # Dummy node to act like
    # parent of root node
    tmp = Node(-1)
    q.append((root, tmp))

    while len(q) > 0:
        # Find number of elements in current level
        levSize = len(q)
        while levSize:

            ele = q.pop(0)

            #check if current node is
            #node a and node b or not

            if ele[0].data == b.data:
                parB = ele[1]

            # push children of currnt node
            if ele[0].data == a.data:
                parA = ele[1]

            # push children of current node into the queue
            if ele[0].left:
                q.append((ele[0].left, ele[0]))
            if ele[0].right:
                q.append((ele[0].right, ele[0]))
            levSize -= 1
            if parA and parB:
                break

            if parA and parB:
                return parA != parB

            if (parA and parB):
                return parA != parB


            if (parA and not parB) or (parB and not parA):
                return False
        return False



# Driver Code
if __name__ =="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(15)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)

    Node1 = root.left.left
    Node2 = root.right.right

    if isCousin(root, Node1, Node2):
        print("yes")
    else:
        print("No")
