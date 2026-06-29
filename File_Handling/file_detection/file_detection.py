# Python File Detection

import os

# Relative path
file_path = "File_Handling/file_detection/readme.txt"

# Check if path exists
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesn't exist")

# Absolute path
file_path = "D:/Codes for Fun/Alarm.py"

# Check if path exists
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    # Check path type
    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory or a folder")
else:
    print("That location doesn't exist")

# Another path
file_path = "D:/Codes for Fun/Bank"

# Check if path exists
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    # Check path type
    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory or a folder")
else:
    print("That location doesn't exist")