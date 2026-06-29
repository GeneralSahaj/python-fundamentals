# Collection = single "variable" used to store multiple values
# list = [] ordered, changeable, allows duplicate members
# set = {} ordered, unchangeable, no duplicate members, add or remove is allowed
# tuple = () ordered, unchangeable, allows duplicate members, FASTER

set = {"pen", "pineapple", "apple", "pen"}

# to list the different functions available for lists, sets, and tuples, we can use the dir() function

#print(dir(tuple))

# to get what each function does, we can use the help() function
#print(help(tuple))

#to get the length of the set, we can use the len() function
print(f"Length of the set: {len(set)}")

#to check if an item is in the set, we can use the in keyword
print(f"Is 'pen' in the set? {'pen' in set}")

#we cannot change the value of an item in the set by using its index as sets are unchangeable

#to add an item to the set, we can use the add() function
set.add("grape")
print(f"Set after adding 'grape': {set}")

#to remove an item from the set, we can use the remove() function
set.remove("grape")
print(f"Set after removing 'grape': {set}")

#pop removes the last item from the set, but since sets are unordered, we cannot be sure which item will be removed
#set.pop()

#to clear the set, we can use the clear() function
#set.clear()

#Some of the above given functions are working as they are not commented out, for other functions you can uncomment them to see how they work.