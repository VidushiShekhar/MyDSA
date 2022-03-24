# python3 implementation of the above approach

# Link list node
class LNode:
    def __init__(self):
        self.data = None
        self.next = None


# A Binary tree Node
class TNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


head = None

def newNode(data):
    node = TNode()
    node.data = data
    node.left = None
    node.right = None

    return node


def preorder(node):

    if node == None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

def push(head ,val):
    new_node = LNode()

    new_node.data = val
    new_node.next = head
    head = new_node
    return head
def printList(node)

# Driver code
# start with the empty list
head = None





