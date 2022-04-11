class node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


preIndex = 0
'''The function to find the value of index 
in arr[start, end]. the function
 assumes that value is present in '''


def search(arr, strt, end, value):

    for i in range(strt, end+1):
        if arr[i] == value:
            return i


# Recursive function to construct a binary tree
def buildTree(inn, pre, inStrt, inEnd):

    global preIndex
    if inStrt > inEnd:
        return None

    # pick current node from preOrder
    tNode = node(pre[preIndex])
    preIndex += 1

    if inStrt == inEnd:
        return tNode
    # Else find the index of this
    inIndex = search(inn, inStrt, inEnd, tNode.data)
    # using index in inorder traversal construct left and right subtree
    tNode.left = buildTree(inn, pre, inStrt, inIndex - 1)
    tNode.right = buildTree(inn, pre, inIndex+1, inEnd)

    return tNode

   # function to compare postorder traversal
def checkPostorder(node, postOrder,index):
    if node == None:
        return index

    index = checkPostorder(node.left, postOrder, index)
    index = checkPostorder(node.right, postOrder, index)

    if node.data == postOrder[index]:
        index += 1
    else:
        return -1

    return index


# driver Code
if __name__ == "__main__":
    inOrder = [4, 2, 5, 1, 3]
    preOrder = [1, 2, 4, 5, 3]
    postOrder = [4, 5, 2, 3, 1]
    lenn = len(inOrder)

    # build the tree from given inorder traversal and preOrder traversal
    root = buildTree(inOrder, preOrder,0, lenn-1)

    # compare postOrder traversal on the constructed Tree
    index = checkPostorder(root, postOrder, 0)

    if index == lenn:
        print("Yes")
    else:
        print("No")

