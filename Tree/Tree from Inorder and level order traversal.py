# construction of Tree using level order traversal

# A binary tree node

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None



def buildTree(level, ino):

    if ino:

        for i in range(0, len(level)):
            if level[i] in ino:
                node = Node(level[i])

                io_index = ino.index(level[i])
                break


        # Construct left and right subtree
        node.left = buildTree(level, ino[0: io_index])
        node.right = buildTree(level, ino[io_index+1: len(ino)])
        return node
    else:
        return None


def printInorder(node):
    if node is None:
        return

    print(node.data, end=" ")

    printInorder(node.right)


# Driver code

levelorder = [20, 8, 22, 4, 12, 10, 14]
inorder = [4, 8, 12, 14, 20, 22]

ino_len = len(inorder)
root = buildTree(levelorder, inorder)

print("Inorder traversal of the constructed tree is")
printInorder(root)








