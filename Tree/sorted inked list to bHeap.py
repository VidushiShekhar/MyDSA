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

def newNode(data) :
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


def printList(node):
    while(node != None):
        print(node.data, end= " ")
        node = node.next

def countLNodes(head):
    count = 0
    temp = head
    while(temp!=None):
        temp = temp.next
        count = count + 1
    return count

def sortedListToBSTRecur(n):
    global head

    if n <= 0:
        return None

    left = sortedListToBSTRecur(n//2)
    root = newNode(head.data)
    root.left = left


    head = head.next

    root.right = sortedListToBSTRecur(n - int(n/2)-1)
    return root




def sortedlistToBST():
    global head

    # count the number of nodes in the linked list
    n = countLNodes(head)

    # Construct BST
    return sortedListToBSTRecur(n)
# Driver code
# start with the empty list
head = None



head = push(head, 7)
head = push(head, 6)
head = push(head, 5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)
head = push(head, 1)
print('The Linked list is: ')
printList(head)
count1 = countLNodes(head)
print(f"\n The number of nodes in the linked list is : {count1}")






