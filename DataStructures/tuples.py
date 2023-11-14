#A tuple stores data as comma seperated elements within parentheses.
#it is immutable, heterogenous, ordered, sequential, and indexed

odd = (1,3,5,7,9)

#immutable: elements cannot be added, removed or modified dynamically
#once a tuple has been initialized, it cannot be changed. This is why they are more memory
#efficient than lists because memory is fixed at the time of creation itself. This also makes
# the lookup activity faster

#Heterogenous: like lists, tuples can hold elements of different data types,
# including different data structures. For example, a tuple couuld have a string,
# followed by a float, followed by a list. Hence, despite a tuple being immutable it can hold mutable objects.
# due to this, data is less tightly packed together (just like in lists)
# ordered: tuples retain the order of elements. Will always be the same as when created
#sequential: they are iterable

data = (1,3, 'strawberry', [9,3,4])
even_nums = 2,4,6,8
print(type(even_nums))
nums = even_nums, (1,3,5,7) #nested tuples
letters = tuple(['a', 'b', 'c'])

#initialize a tuple with only one element
#if done without a comma, it won't create a tuple
single = 1,
single_test = (1)
type(single_test)

#unpacking a tuple (storing its values into individual variables)
a,b,c,d = even_nums
print(a,b,c,d)

tuple = (1,2,3,1)

tuple.count(1)
tuple.index(1)

