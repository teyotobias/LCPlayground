#NEED TO GO OVER HEAPS AGAIN : gone over, information directly below

#python uses min-heaps by default

#while heapq provides min-heap by default, you can simulate a max-heap by inverting the order using negative numbers. For example, if you wanted to 
#insert an element into a max-heap, you would insert its negative, and similarily, when you retrieve an element, you would take its negative to get the actual value

#heaps are like binary trees that are ordered by value. In min-heaps, the head (top node) is the smallest value. In max-heaps, the largest is at the top.
#in min-heaps, parents are less than or equal to their children
#in max-heaps, parents are more than or equal to their children

# Heap data structure is used to implement the Priority
# Queue ADT. In python we can directly access a Priority Queue
# implemented using a Heap by using the Heapq library/module

#using heaps.heapify() can reduce both time and space complexity because
# heaps.heapify() is an in place heapify and costs linear time to run it
#both heapq.heappush() and heapq.heappop() cost O(logN) time complexity

#Total time complexity is O((N-k)logN), total space O(1)

import heapq #(minHeap by Default)

nums = [5,7,9,1,3]
heapq.heapify(nums) #converts list into heap. Can be converted back to list by list(nums)
print(nums)
#heapq.heappush(nums, element) push an element into the heap
heapq.heappush(nums, 10)
print(nums)
heapq.heappop(nums) #pop an element from the heap (from the front)
print(nums)



nums1 = [3,1,4,1,5,9,2,6,5,3,5]
heapq.heapify(nums1) #transforms list in-place into a heap

#insert an element into the heap
heapq.heappush(nums1, 7)

#pops the smallest element
smallest = heapq.heappop(nums1)
print(smallest)

#find the three largest numbers in an iterable
print(heapq.nlargest(3, nums)) #outputs [9,6,7]
#heappush(heap, ele) :- this function is used to insert the element mentioned in its arguments into heap. The order
# is adjusted, so as heap structure is maintained.

#heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted,
# so as heap structure is maintained



#Other methods available in the library
#used to return the k largest elements from the iterable specified
#the key is a function with that accepts single element from iterable,
# and the returned value from that function is then used to rank that element in the heap

# heapq.nlargest(k, iterable, key = fun)

# heapq.nsmallest(k, iterable, key = fun)