# working of heapq
from heapq import heapify, heappush, heappop

# create an empty heap
heap = []
heapify(heap)

# Adding items to the heap using heappush function
heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 40)
heappush(heap, 90)
heappush(heap, 14)
heappush(heap, 80)

print(f"Head value of  heap: {heap[0]} ")

# printing the elements of the heap
print("The heap elements: ")
for i in heap:
    print(i, end=' ')
print('\n')

element = heappop(heap)

print("The heap elements :")
for i in heap:
    print(i, end=' ')


