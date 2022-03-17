'''A min heap is a complete binary tree ,It is typically represented by an arry .The root element will be arr[0'''
'''Opeartion of Min Heap
1. getMin()
2.extractMin()
3.insert()'''
import sys


class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1*sys.maxsize
        self.Front = 1

    def parent(self, pos):
        return pos//2


    # function to find the left child
    def leftChild(self, pos):
        return 2 * pos
    # function to find the right child


    def rightChild(self, pos):
        return (2*pos) + 1
    # function to identify the leaf


    def isLeaf(self, pos):
        return pos*2 > self.size
    # function to swap the position


    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        #  if the node is a non leftNode and greater than the child
        if not self.isLeaf(pos):
            if(self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] > self.Heap[self.rightChild(pos)]):
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))



    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)


    def print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))



    def minHeap(self):
        for pos in range(self.size//2, 0,-1):
            self.minHeapify(pos)



    def remove(self):
        popped = self.Heap[self.Front]
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.Front)
        return popped

# Driver Code:
if __name__ =='__main__':
    print("The minheap is")
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.minHeap()

    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))


