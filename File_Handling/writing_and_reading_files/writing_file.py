#Python Writing files (.txt, .json, .csv)

import json
import csv

# =========================
# TXT FILE
# =========================

text_data = """Hello!
This is a text file.
I am learning File Handling in Python.
"""

txt_path = "File_Handling/writing_and_reading_files/output_input.txt"

try:
    with open(txt_path, "w") as file:     #"w" this mode is for writing it will write text in the file and if any text exists it will overwrite it

        # Writes plain text into the file
        file.write(text_data)

    print(f"TXT file '{txt_path}' was created")

except Exception as e:
    print(e)


# =========================
# JSON FILE
# =========================

student = {
    "name": "Sahaj",
    "age": 20,
    "course": "Gaming Technology"
}

json_path = "File_Handling/writing_and_reading_files/output_input.json"

try:
    with open(json_path, "w") as file:                            #"w" this mode is for writing it will write text in the file and if any text exists it will overwrite it

        # Converts a Python object into JSON
        # and writes it into the file
        json.dump(student, file, indent=4)

    print(f"JSON file '{json_path}' was created")

except Exception as e:
    print(e)


# =========================
# CSV FILE
# =========================

employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]

csv_path = "File_Handling/writing_and_reading_files/output_input.csv"

try:
    with open(csv_path, "w", newline="") as file:                             #"w" this mode is for writing it will write text in the file and if any text exists it will overwrite it

        # Creates a helper object that knows
        # how to format data as CSV
        writer = csv.writer(file)

        # Writes one row at a time
        for row in employees:
            writer.writerow(row)

    print(f"CSV file '{csv_path}' was created")

except Exception as e:
    print(e)