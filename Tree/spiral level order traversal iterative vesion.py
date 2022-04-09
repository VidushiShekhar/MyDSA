class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printSpiral(root):
    if root == None:
        return
    # stacks to store alternate level
    s1 = []# from right to left

    s2 = []# from left to right

    s1.append(root)
    while not len(s1) == 0 or not len(s2) == 0:
        while not len(s1) == 0:
            temp = s1[-1]
            s1.pop()
            print(temp.data, end=' ')

        if temp.right:
            s2.append(temp.right)
        if temp.left:
             s2.append(temp.left)

    while not len(s2) == 0:
           temp = s2[-1]
           s2.pop()
           print(temp.data, end=" ")

           if temp.left:
               s1.append(temp.left)
           if temp.right:
               s1.append(temp.right)


# Driver Code:
if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)
    print("Spiral order traversal of "
          "binary tree")

    printSpiral(root)


