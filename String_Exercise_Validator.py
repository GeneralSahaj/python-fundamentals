# Validate user input exercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Username must be no more than 12 characters.")

elif not username.find(" ") == -1:
    print("Username must not contain spaces.")

elif not username.isalpha():
    print("Username must not contain digits.")

else:
    print("Username is valid.")
    print(f"Welcome, {username}!")