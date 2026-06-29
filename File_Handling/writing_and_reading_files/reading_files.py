# Pyhton Reading Files (.txt, .json, .csv)

import json
import csv

file_path = "File_Handling/writing_and_reading_files/output_input.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")


file_path = "File_Handling/writing_and_reading_files/output_input.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

print()


file_path = "File_Handling/writing_and_reading_files/output_input.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")