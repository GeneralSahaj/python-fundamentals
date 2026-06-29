# Collection = single "variable" used to store multiple values
# list = [] ordered, changeable, allows duplicate members
# set = {} ordered, unchangeable, no duplicate members, add or remove is allowed
# tuple = () ordered, unchangeable, allows duplicate members, FASTER

tuple = ("pen", "pineapple", "apple", "pen")

# to list the different functions available for lists, sets, and tuples, we can use the dir() function

#print(dir(tuple))

# to get what each function does, we can use the help() function
#print(help(tuple))

#to get the length of the tuple, we can use the len() function
print(f"Length of the tuple: {len(tuple)}")

#to check if an item is in the tuple, we can use the in keyword
print(f"Is 'pen' in the tuple? {'pen' in tuple}")

# to check the index of an item in the tuple, we can use the index() function
print(f"Index of 'pineapple': {tuple.index('pineapple')}")

# to count the number of times an item appears in the tuple, we can use the count() function
print(f"Count of 'pen': {tuple.count('pen')}")