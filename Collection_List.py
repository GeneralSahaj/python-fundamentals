# Collection = single "variable" used to store multiple values
# list = [] ordered, changeable, allows duplicate members
# set = {} ordered, unchangeable, no duplicate members, add or remove is allowed
# tuple = () ordered, unchangeable, allows duplicate members, FASTER

list = ["pen", "pineapple", "apple", "pen"]

# to list the different functions available for lists, sets, and tuples, we can use the dir() function

#print(dir(list))

# to get what each function does, we can use the help() function
#print(help(list))

#to get the length of the list, we can use the len() function
print(f"Length of the list: {len(list)}")

#to check if an item is in the list, we can use the in keyword
print(f"Is 'pen' in the list? {'pen' in list}")

#we can also change the value of an item in the list by using its index
#list[0] = "pencil"

#to add an item to the end of the list, we can use the append() function
#list.append("grape")

#to remove an item from the list, we can use the remove() function
#list.remove("apple")

#to insert an item at a specific index, we can use the insert() function
#list.insert(1, "grape")

# to clear the list, we can use the clear() function
#list.clear()

# to get the index of an item in the list, we can use the index() function
print(f"Index of 'pineapple': {list.index('pineapple')}")

# to count the number of times an item appears in the list, we can use the count() function
print(f"Count of 'pen': {list.count('pen')}")

#Some of the above given functions are working as they are not commented out, for other functions you can uncomment them to see how they work.