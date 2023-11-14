# assert keyword is used when debugging code:
x = "hello"
#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"

# Input

feedback = input("How are we doing")
print(feedback)

# Multiline input in python 
    # using split method + list comprehension

x,y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at a time
x,y,z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is :", y)
print("Number of girls is: ", z)

# 2 inputs again
a,b = input("Enter a two value: ").split()
print("First number is {} and second number is {}").format(a,b)

#taking multiple inputs at a time and type casting using list() function
x = list(map(int, input("Enter a multiple value").split()))
print("List of students: ", x)


#taking multiple input using List comprehension

x,y = [int(x) for x in input("Enter two value: ").split()]


#3 input

x, y, z = [int(x) for x in input("Enter three value").split()]

x,y = [int(x) for x in input("Enter 2 values").split()]
print("First number is {} and the second number is {}".format(x,y))

# math functions

# Printing the log base e of 14
import math
print(math.log(14))

# printing log base 5 of 14
print(math.log(14,5))

# find ceiling and floor value
# ceil means smallest integral value greater than the number and the floor value means the greatest integer value smaller than yours

a = 2.3

print(math.ceil(a)) #will return 3

print(math.floor(a)) # will return 2

# value of Euler 2 : 2.71828....
print(math.e)

# pi
print(math.pi)

# returns binary version of number
bin(512)

# divmod(int, int) returns tuple like (quotient, remainder)

# HOW does the custom comparator work?


# When providing a custom comparator, it should generally return an integer/float value that follows the following pattern (as with most other programming languages and frameworks):

# return a negative value (< 0) when the left item should be sorted before the right item
# return a positive value (> 0) when the left item should be sorted after the right item
# return 0 when both the left and the right item have the same weight and should be ordered "equally" without precedence
