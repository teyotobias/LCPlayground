#Deque - a double ended queue has the feature of adding and removing
#elements from either end

#A deque is represented internally as a double linked list. Both ends
# are accesible, but even looking at the middle is slow, and adding to or
# removing from the middle is slower still

from collections import deque

queue = deque(['name', 'age', 'DOB'])
print(queue)
queue.append("append_from_right") #append from the right
print(queue)
queue.pop() #pop from right
print(queue)
queue.appendleft("fromLeft") #append from left
print(queue)
queue.popleft() #pop from left
print(queue)

#returns first index of element between 2 indices
# queue.index(element, begin_index, end_index)

#inserts an element at specified index
#queue.insert(index, element) 
queue.remove('age') #removes first occurance of specified element
print(queue)
print(queue.count('DOB')) #counts number of element in the queue
queue.reverse() #reverses order of queue elements
print(queue)