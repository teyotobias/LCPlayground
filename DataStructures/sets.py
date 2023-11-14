#A set is a collection of comma seperated, unordered, unique elements within curly brackets.
#it is mutable, unindexed, and heterogenous

set = {1,2,3}

set.add(4)
set.remove(4)
# set.discard and set.remove basically do the same thing | remove will throw error if element is not there | discard will not
# set.discard(4)
set.pop() #removes random item (since unordered)
set2 = {1,2,3,4,5,6}

set.isdisjoint(set2) #returns true if no common elements
set.issubset(set2) #returns true if all elements from set2 is in original set
set.issuperset(set2) #returns true if all elements from original set is present in set2

set.difference(set2) #returns everything set containing items ONLY in first set
set.difference_update(set2) #removes common elements from first set [no new set is created or returned]
set.intersection(set2) #returns new set with common elements
set.intersection_update(set2) #modifies first set keeping only common elements
set.symmetric_difference(set2) # returns set containing all non-common elements of both sets
set.symmetric_difference_update(set2) #same as symmetric_difference but changes are made on original set
set.union(set2) #combines sets 
set.update(set2) #adds set2 without duplicate