# For loops = execute a block of code a fixed number of times.
#             you can iterate over a range,string, sequence, or other iterable object.

# Basic syntax:
# for x in range(start, end, step):
#     print(x)

#Example 1
for x in range(1, 11):
    print(x)

# Reverse order
print("\nCountdown:\n")
for x in reversed(range(1, 11)):
    print(x)

print("Happy new year!")

# Skipping over an iteration
print("\nskipping unlucky number 13:\n")

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)