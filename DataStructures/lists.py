#a list stores data as comma seperated elements with square brackets. It is an ordered (by insertion, not value),
# sequential, heterogenous, indexed, mutable, non-unique data structure
# ordered: a list maintains the order of elements as you insert them
#sequential: a list can be iterated over
#mutable : the items can be changed
#non-unique: the same element can appear more than once in a list

# .append(x)
numbers = [1,2,3]
numbers.append(4) #[1,2,3,4]

# .extend(iterable)
numbers.extend([5,6]) # [1,2,3,4,5,6]

# extend with a tuple:
numbers.extend(7,8) # numbers = [1,2,3,4,5,6,7,8]

# .insert(i, x)
numbers.insert(2, 'a') # [1,2,'a',3,4,5,6]

# .remove(x)
numbers.remove('a') # [1,2,3,4,5,6]

# .pop([i]) - can be invoked w/ index or without
last = numbers.pop() # [1,2,3,4,5], 6 in 'last'
# can also specify the index to pop
last2 = numbers.pop(3) # [1,2,3,5] #popped 4 since it was at index 3

# .clear()
numbers.clear() # []

# .index(x[, start[, end]]) , use square brackets when you want to look in a specific frame of the array
a = ['a', 'b', 'c', 'b']

index_b = a.index('b')  # 1
index_b_sub = a.index('b', 2) # 3

# .count(x)
count = [1,2,1,1,2,3,5,6].count(1) #3
# can also do on existing list:
a.count('b')

# .sort(key=None, reverse=False)
[3,1,4,1,5].sort() 
#sort in reverse order (descending order)
numbers.sort(reverse=True)

# sort by length
words = ['apple', 'pear', 'banana']
words.sort(key=len) # ['pear', 'apple', 'banana']

# sort a list of tuples based on the second element of each tuple
tuples = [(1, 'pear'), (2, 'apple'), (3, 'banana')]

tuples.sort(key=lambda x: x[1]) # [(2, 'apple'), (3, 'banana'), (1, 'pear')]

# Sort dictionary by keys and get a list of tuples
d = {'apple': 3, 'banana': 2, 'pear': 1}
sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # [('apple', 3), ('banana', 2), ('pear', 1)]

# Sort dictionary by values
sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # [('pear', 1), ('banana', 2), ('apple', 3)]

# The 'sorted()' function returns a new sorted list from the elements of any iterable, without modifying the original iterable
unsorted_list = [3,1,4,1,5]
sorted_list = sorted(unsorted_list)

# Sorting complex objects
class Fruit:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
fruits = [Fruit('apple', 5), Fruit('banana', 2), Fruit('pear', 3)]
fruits.sort(key=lambda fruit: fruit.quantity) # Sort by quantity

# .reverse()
[1,2,3].reverse() # [3,2,1]

# .copy() 
original = [1,2,3]
copy = original.copy() # [1,2,3]





























nums = [1,2,3]

print(nums.index(1)) #returns index of specified value
nums.append(1) #appends 1 to list
nums.insert(0, 10) #inserts 10 at 0th index
nums.remove(3) #removes value from list
nums2 = nums.copy() #returns a copy of the list
#list comprehensions
squares = [x**2 for x in range(1,41)]
nums3 = [num for num in squares if num%2==0]
result = [num if num%2==0 else 'no' for num in squares]

print(nums2)
print(nums.count(1)) #counts the number of occurences of the provided value in the list
nums.extend(nums2) #adds specified list to the end of nums
print(nums)
nums.pop() #pops last element (which element to pop can also be given as an optional argument)
nums.reverse() #reverses original list (nums in this case)
print(nums)
nums.sort() #sorts list (doesn't return ordered list - modifies in place)
print(nums)

#indexingm- can also "slice"
print(nums) #full list

#nums[stop:start]
print(nums[0:3]) #prints first 3 numbers
#nums[start:]
print(nums[3:]) #prints the rest of the lsit
#nums[:stop]
print(nums[:3]) #will print the same thing as first example, all elements up to index 3
#nums[:]
print(nums[:]) #prints the whole array
#nums[-1]
print(nums[-1]) #prints the last element of the list