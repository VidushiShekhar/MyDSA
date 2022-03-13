class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    current = root
    stack = [] # initialize the stack
    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack ;however if stack is empty we are done
        elif (stack):
            current = stack.pop()
            print(current.data, end=' ')
            current = current.right
# both stack is empty and current is null
        else:
            break

    print()

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)