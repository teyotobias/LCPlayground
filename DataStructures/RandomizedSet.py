#REMEMBER ALWAYS TO PUT SELF IN FUNCTION DEFINITIONS FOR A CLASS
import random
#all functions need to be O(1)
class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.vals_to_index = {}
        #constructor function
    
#maps in square brackets
#lists in square brackets
    def insert(self, val):
        #insert function
        #if you check for existence inside lists, it will be O(N)
        #USE MAP CHECK INSTEAD FOR 0(1)
        # if val in self.vals:
        if val in self.vals_to_index:
            return False
        self.vals_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True
    
    def remove(self, val):
        # if val not in self.vals:
        if val not in self.vals_to_index:
            return False
        index = self.vals_to_index[val]
        last_val = self.vals[-1]
        self.vals[index] = last_val
        self.vals_to_index[last_val] = index
        self.vals.pop()
        del self.vals_to_index[val]
        return True

        #remove random value
        #for O(1): need to do inplace
    

    def getRandom(self):
        #get and return a random value
        return random.choice(self.vals)
    



# Usage:
# Commands and arguments will be input as per the example you provided.
# This code will create a RandomizedSet instance and call the specified methods with the provided arguments.
commands = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
args = [[], [1], [2], [2], [], [1], [2], []]

randomizedSet = None
output = []

for cmd, arg in zip(commands, args):
    if cmd == "RandomizedSet":
        randomizedSet = RandomizedSet() #initializing objects in python0
        output.append(None)
    elif cmd == "insert":
        output.append(randomizedSet.insert(*arg))
    elif cmd == "remove":
        output.append(randomizedSet.remove(*arg))
    elif cmd == "getRandom":
        output.append(randomizedSet.getRandom())

print(output)  # Output: [null, True, False, True, 2, True, False, 2]
