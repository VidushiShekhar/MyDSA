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
            temp = root_node.customList[index]
            root_node.customList[index] = root_node.customList[parentIndex]
            root_node.customList[parentIndex] = temp


    elif heapType == "Max":
        if root_node.customList[index] > root_node.customList[parentIndex]:
            temp = root_node.customList[index]
            root_node.customList[index] = root_node.customList[parentIndex]
            root_node.customList[parentIndex] = temp

        heapifyTreeInsert(root_node, parentIndex, heapType)

# Function to insert a Node in the Binary Heap
def insertNode(root_node, nodeValue, heapType):
    if root_node.heapSize + 1 == root_node.maxSize:
        return " The Binary Heap is fully occupied"
    root_node.customList[root_node.heapSize + 1] = nodeValue
    root_node.heapSize +=1
    heapifyTreeInsert(root_node,root_node.heapSize, heapType)
    return "The node was inserted successfully "

## Initializing a Binary Heap
newHeap = BHeap(10)
insertNode(newHeap, 70, 'Max')
insertNode(newHeap, 40, "Max")
insertNode(newHeap, 30, "Max")
insertNode(newHeap, 60, "Max")
insertNode(newHeap, 80, "Max")
insertNode(newHeap, 20, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 50, "Max")
insertNode(newHeap, 10, "Max")
levelOrderTraversal(newHeap)



# Function to heapify the binary Heap while Extraction

def heapifyTreeExtract(root_node, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if root_node.heapSize < leftIndex:
        return
    elif root_node.heapSize == leftIndex:
        if heapType == "Min":
            if root_node.customList[index] > root_node.customList[leftIndex]:
                temp = root_node.customList[index]
                root_node.customList[index] = root_node.customList[leftIndex]
                root_node.customList[leftIndex] = temp
            return
        else:
            if root_node.customList[index] < root_node.customList[leftIndex]:
                temp = root_node.customList[index]
                root_node.customList[index] = root_node.customList[leftIndex]
                root_node.customList[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if root_node.customList[leftIndex] < root_node.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if root_node.customList[index] > root_node.customList[swapChild]:
                temp = root_node.customList[index]
                root_node.customList[index] = root_node.customList[swapChild]
                root_node.customList[swapChild] = temp
        else:
            if root_node.customList[leftIndex] > root_node.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if root_node.customList[index] < root_node.customList[swapChild]:
                temp = root_node.customList[index]
                root_node.customList[index] = root_node.customList[swapChild]
                root_node.customList[swapChild] = temp
    heapifyTreeExtract(root_node, swapChild, heapType)







# Function to extarct a Node from Binary Heap
def extractNode(root_node, heapType):
    if root_node.heapSize == 0:
        return " The Binary Tree is empty"
    else:
        extractedNode = root_node.customList[1]
        root_node.customlist[1] = root_node.customlist[root_node.heapSize]
        root_node.customlist[root_node.heapSize] = None
        root_node.heapSize -= 1
        heapifyTreeExtract(root_node, 1, heapType)
        return extractedNode


# Clearing of Entire Binary Heap
# simply set Basic list to None
def deleteEntireBP(root_node):
    root_node.customlist = None
    print("The Binary Heap has Been Successfully Deleted")



