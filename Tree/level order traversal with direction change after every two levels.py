from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = self.right = None



def modifiedLevelOrder(node):
    if node == None:
        return
    if node.left == None and node.right == None:
        print(node.data, end=' ')
        return

    myQueue = deque()

    myStack = []
    temp = None
    sz = 0
    ct = 0
    # used for changing the direction of the level order traversal
    rightToleft = False

    myQueue.append(node)
    while(len(myQueue)> 0):
        ct +=1
        sz = len(myQueue)

        #Do normal level order traversal
        for i in range(sz):
            temp = myQueue.popleft()


            if rightToleft == False:
                print(temp.data, end=" ")


            else:
                myStack.append(temp)
            if temp.left:
                myQueue.append(temp.left)

            if temp.right:
                myQueue.append(temp.right)

        if rightToleft == True:

            while len(myStack) >0:
                temp = myStack[-1]

                del myStack[-1]
                print(temp.data, end=" ")

        if ct == 2:
            rightToleft = not rightToleft
            ct = 0

        print()

if __name__ =="__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(3)
    root.left.right.right = Node(1)
    root.right.left.left = Node(4)
    root.right.left.right = Node(2)
    root.right.right.left = Node(7)
    root.right.right.right = Node(2)
    root.left.right.left.left = Node(16)
    root.left.right.left.right = Node(17)
    root.right.left.right.left = Node(18)
    root.right.right.left.right = Node(19)

    modifiedLevelOrder(root)
