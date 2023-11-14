#a dictionary stores data in the form of key-value pairs. It is a sequential, heterogenous, 
# unordered, indexed, mutable data structure

dict = {'a': 1, 'b': 2, 'c': 3} #declare a dict


print(dict.keys()) #print the dictionary's keys - EO:  a, b, c
print(dict.values()) #returns the dictionary's values - EO: 1,2,3
print(dict.get('a')) #gets value with key 'a' - EO: 1
print(dict.items()) #gets all key-value pairs - EO: Everything
dict2 = dict.copy() #returns a copy of the dictionary
print(dict2)
dict.pop('a') #pops pair with key 'a' from the dictionary
print(dict) # EO - b, c
dict.popitem() #removes most recent pair added
print(dict) # EO - b
# dict.setDefault(KEY, DEFAULT_PAIR)
# returns value of key, if key exists, else default value returned
# If the key exist, this parameter(DEFAULT_VALUE) has no effect.
# If the key does not exist, DEFAULT_VALUE becomes the key's value. 2nd argument's default is None.
dict.update({'b':20}) 
print(dict.items())  # EO: b 20
print(dict2) #EO - a 1 b 2 c 3

#Counter - Python counter is a container that will hold the count of each of
# the elements present in the container. The counter is a sub-class available
# inside the dictionary class. Specifically used for element frequencies
#similar to dictionary, defaultdict(int) is used most of the time

from collections import Counter
import collections
#can be used as collections.Counter() in code as well

list4 = ['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z']
#init
Counter(list4) # -> Counter({'x': 4, 'y': 2, 'z': 2})
Counter('Welcome to Guru99 Tutorials!') # -> Counter({'o':3, ' ' : 3, 'u':3, 'e':2})

#updating
counterObject = collections.Counter(list4)

counterObject.keys = ['x', 'y', 'z']
most_common_element = counterObject.most_common(1) # [('x', 4)]
print(most_common_element)
counterObject.update("some string") # -> Counter('o': 3, 'u': 3, 'e': 2, 's': 2) -> leaves previous values in there
print(counterObject)
counterObject['s'] += 1

#accessing
frequency_of_s = counterObject['s']

#deleting: 
del counterObject['s']