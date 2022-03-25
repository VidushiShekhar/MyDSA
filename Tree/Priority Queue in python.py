import heapq
# list initializing

li = [5, 7, 9, 1, 3]

heapq.heapify(li)

print("The heap made is :", end=" ")
print(list(li))

heapq.heappush(li, 4)
print("The modified heap push is: ", end=" ")
print(list(li))

print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))

'''heappushpop(heap,ele): Increase efficiency function combines the functioning
 of both push and op operations in one statement
 heapreplace(heap, ele): same as above but the 
 value larger than the pushed value can be returned as 
 pop is performed first than push'''
li1 = li
print("List1 is: ", end=" ")
print(li1)
print("The popped item using heappushpop() is:", end=" ")
print(heapq.heappushpop(li, 2))
print('The popped element using heapreplace is: ', end=" ")
print(heapq.heapreplace(li1, 2))

print("The 3 largest numbers in the list are:", end=" ")
print(heapq.nlargest(3, li1))

print("The 3 smallest numbers in list are: ", end=' ')
print(heapq.nsmallest(3, li1))
