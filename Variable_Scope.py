# Variable Scope = where a variable is visible and accessible
# Scope Resolution = (LEGB Rule) Local -> Enclosing -> Global -> Built-in

def func1():
    x = 10 # Local variable (Priority 1)
    print("Inside func1:", x)
    def func2():
        print("Inside func2:", x) # Enclosing variable (Priority 2)
    func2()

x = 20 # Global variable (Priority 3)

func1()

# Built-in variable (Priority 4)
from math import pi
print("Built-in variable (pi):", pi)

print()

print("Look how the global variable was ignored in func1 and func2 as they have their own local and enclosing variables with the same name.")
print()
print("To see global variable in terminal from func1 and func2, comment out the local variable declarations.")
print()