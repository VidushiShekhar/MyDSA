from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Using of stacks an queue
def reverseLevelOrder(root):
    q = deque()
    q.append(root)
    global ans
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:
            continue

        ans.appendleft(node.data)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)

    return ans


# Driver program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Level order traversal of a binary tree: ")
reverseLevelOrder(root)
for i in ans:
    print(i, end=" ")
