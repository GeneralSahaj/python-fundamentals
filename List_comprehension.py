# List comprehension =  a concise way  to create lists in python.
#                       Compact and easier to read than traditional loops
#                       Syntax = [expression for item in iterable if condition]

# The Syntax can be read as "Do this (expression) for each (item) in this (iterable) if this condition is true"

# Example 1
# double the numbers in a list

# double = [x * 2 for x in range(1, 11)]

# print(double)

fruits = ["orange", "apples", "banana", "coconut"]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)

students = {"Jane": 100, "Cho": 90, "Teresa": 75, "Van Pelt": 50, "Rigsby": 45}

passed_students = {student for student in students if students[student] >= 60}

print(passed_students)