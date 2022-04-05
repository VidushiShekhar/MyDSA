# First make the tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

# define the ZigZag traversal algorithm
def ZigZag(root):

    if root is None:
        return
    # 2 stacks initialized
    curr = []
    next1 = []

    # push the root
    curr.append(root)
    # direction variable
    isLtoR =True
    while len(curr) != 0:
        # pop from stack
        temp = curr.pop(-1)
        # if temp exists print temp
        print(temp.data)

        # pushing the nodes in next
        if isLtoR ==True:
            if temp.left_node != None:
                next1.append(temp.left_node)
            if temp.right_node != None:
                next1.append(temp.right_node)
        else:
            if temp.right_node != None:
                next1.append(temp.right_node)
            if temp.left_node != None:
                next1.append(temp.left_node)


        # check if curr is empty
        if len(curr) == 0:
            isLtoR = not isLtoR
            curr, next1 = next1, curr






# Define a tree to traverse the algorithm on
root = Node(4)
root.left_node = Node(2)
root.right_node = Node(5)
root.left_node.left_node = Node(1)
root.right_node.right_node = Node(3)
print("ZigZag Traversal:")
ZigZag(root)