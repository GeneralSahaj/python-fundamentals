# Arbitrary Arguments:
# *args allows a function to accept any number of positional arguments.
# **kwargs allows a function to accept any number of keyword arguments.
# This makes the function flexible because the exact number of arguments
# does not need to be known beforehand.

# *args = allows user to pass multiple non key arguments
# **kwargs = allows user to pass multiple key arguments (keyword arguments)
#           * unpacking operator = unpacks the values from a list, tuple,
#           or dictionary and passes them as separate arguments to a function.
#                    1. Positional 2. Default 3. Keyword 4. ARBITRARY


# Function definition
# *args collects extra positional arguments into a tuple
# **kwargs collects extra keyword arguments into a dictionary
def shipping_label(*args, **kwargs):

    # Display heading
    print("Shipping to:")

    # Loop through all positional arguments
    # and print each one
    for arg in args:
        print(arg)

    # Display heading for keyword details
    print("\nDetails:")

    # Loop through all keyword arguments
    # .items() returns both the key and value
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Program starts executing here

# Positional arguments are stored in args
# Keyword arguments are stored in kwargs
shipping_label(
    "Sahaj Singh",
    "123 Main St",
    "Anytown, India",
    weight="2kg",
    delivery_date="2026-07-01"
)