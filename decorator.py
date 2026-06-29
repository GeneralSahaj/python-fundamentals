# Decorator = A function that extends the behavior of another function
#             without modifying the base function
#             Pass the base function as an argument to the decorator

# defination of Decorator is that Decorator is a function that takes another function as arguments and returns a function

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("* You added sprinkles 🎊 *")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("* You added fudge 🍫 *")
        func(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print (f"Here is your {flavor} ice cream 🍨")

get_ice_cream("Chocolate")