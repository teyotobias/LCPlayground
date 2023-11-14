#lists

#how many data types does python have?
    #numeric boolean string sequence (strings, lists, tuples)
#types: Ints, floats, strings, 
x = 5
print(type(x))
y = "hello"
print(type(y))
z = 'hello'
print(type(z))

#transform to int
print(int("54"))

#print several strings
print(z + "there")

#integer to string
print(str(x) + " dollars")

#lists can store all data types - cannot do sort on this sort of object unless overwritten?
list4 = ['hello',4,5,6,'nice']
print(list4)


#unordered
list1 = [3,4,5,6,2,1]
print(list1)

#reassignable and duplicates allowed
list1 = [4,4,4,4,4]
print(list1)

list1 = [3,4,5,6,2,1]

#sort list values
list1.sort()
print(list1)

list2 = [4,5,2,3,45,6,1,4,9,3]
#adds so that total length = m + n
list3 = list1 + list2
print(list3)
list3.sort()
#add an element
list3.append(5)
print(list3)

#removes item and returns item at index (default: last)
element = list3.pop()
print(element)
print(list3)
#inserts object before index provided as first argument
list3.insert(1, 100)
print(list3)

#removes only first occurence of value
list3.remove(1)
print(list3)

#counts the number of occurences of provided value in the list
fourCounter = list3.count(4)
print(fourCounter)

#extends list -> adds more than one value at a time (adds in random order)
list3.extend({46,47,48,49})
print(list3)


