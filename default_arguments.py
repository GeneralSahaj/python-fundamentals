## Default argument = a default value for certain parameters.
#                    default is used when that argument is omitted.
#                    Make your function more flexible by reducing the number of arguments, 
#                    1) positional 2) default  3) keywords 4) arbitrary 

# Default Argument:
# A parameter can be given a default value when the function is defined.
# If an argument for that parameter is not provided when the function is called,
# Python automatically uses the default value instead.



import time

def count(end, start = 0):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Done!")


count(5) # start = 0 by default
count(5, 2) # start = 2, overrides the default value