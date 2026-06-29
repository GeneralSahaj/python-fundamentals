# Membership operator = used to test whether a value or variable is present in a sequence  
#                       (string, list, tuple, set and dictionary)
#                       Two membership operators
#                       in      = Returns True if a sequence with the specified value is present in the object
#                       not in  = Returns True if a sequence with the specified value is not present in the object

# Example code

email = "sahajsingh@gmail.com"

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")

