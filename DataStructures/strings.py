# SPLIT
text = 'Python is a fun programming language'


print(text.split(' '))

# STRING TO LIST
s = "abcd"
s = list(s)

# COUNT

message = 'python is popular programming language'
print('Number of occurences of p: ', message.count('p'))

s= '1242323'
print(s.isnumeric())

#FIND - returns index of first occurrence of substring if found
#if not, returns -1
print(text.find('fun'))

#the ISALNUM() method returns True if all characters in the string are alphanumeric (either alphabet or number)
#if not, it returns false
name = "M3nica Gell22er "
print(name.isalnum()) #returns false -> because of the spaces

#the ISALPHA() method returns true if all characters in the string are alphabets
# if not, returns false
name = "Monica"
print(name.isalpha())

#other important functions

# UPPER() - convert all to uppercase
print(name.upper())

# LOWER() - convert all to lowercase
print(name.lower())

#check for lowercases: ISLOWER()
print(name.islower()) # should return false
# ISDIGIT() - check for all numbers
print(name.isdigit()) # should return false

# ISUPPER() - check for all uppercase
print(name.isupper()) # should return false

#BUILT IN OR LIBRARY FUNCTIONS

# ord(str) -> returns ascii value of the character

# chr(int) -> return character of given ascii value

# filter(function, list) -> returns list with element that returned true when passed into function

# enumerate(list) -> when you need to attach indexes to lists or tuples
# ['a', 'b', 'c'] -> [(0, 'a'), (1, 'b'), (2,'c')]

# any(list) # returns true if ANY element in list is true (any string, all numbers except 0 also count as true)