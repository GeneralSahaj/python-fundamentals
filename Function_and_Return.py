# Function = A block of reusable code
#            place () after the function name to invoke it
# return = statement used to end a function and send a result back to the caller

# Positional Arguments:
# Values are matched to parameters based on their position.
# The first value goes to the first parameter, the second value
# goes to the second parameter, and so on.


# Function definition
# This code is stored and will only run when the function is called
def create_name(first, last):

    # Capitalize the first letter of both names
    first = first.capitalize()
    last = last.capitalize()

    # End the function and send the full name back
    return first + " " + last


# Program starts executing here

# Get the user's first name
first_name = input("Enter your first name: ")

# Get the user's last name
last_name = input("Enter your last name: ")

# Call the function and pass the user's inputs as arguments
# The returned full name is stored in full_name
full_name = create_name(first_name, last_name)

# Display the result
print(f"Your full name is {full_name}")