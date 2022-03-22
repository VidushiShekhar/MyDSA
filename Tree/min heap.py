class BHeap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


newBinaryHeap = BHeap(5)

# Function to find the peek in the binary Heap


def peekofBHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]


# size of binary heap:
def sizeOfBHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize
print(sizeOfBHeap(newBinaryHeap))


# level order Traversal in Binary Heap
'''The level order traversal is the breadth first traversal
 where nodes are visited level-by-level.then 
 they are traversed in a left to right manner'''

# Function to perform level order traversal in Binary heap
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])


def heapifyTreeInsert(root_node, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if root_node.customList[index] < root_node.customList[parentIndex]:
            root_node.customList[index] = root_node.customList[parentIndex]




