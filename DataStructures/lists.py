#a list stores data as comma seperated elements with square brackets. It is an ordered (by insertion, not value),
# sequential, heterogenous, indexed, mutable, non-unique data structure
# ordered: a list maintains the order of elements as you insert them
#sequential: a list can be iterated over
#mutable : the items can be changed
#non-unique: the same element can appear more than once in a list

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
print(nums.count(1)) #counts the numbero of occurences of the provided value in the list
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