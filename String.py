name = input("Pura Naam bata tera: ")

print("sun be chirkut")

length = len(name)
print(f"Tera naam {length} akshar ka hai pura spacing mila ke")

space = name.find(" ")

if space>=0:
    space_human = space + 1

    print(f"tere naam me space {space} number pe hai, insani bhasha me bole to {space_human} pe hai")

else:
    print("Chahe toh tereko padhna nahi ata kyuki tere pura naam manga tha, ya tere naam  me surname nahi hai jaise teri life me koi nahi hai")

#other boring string functions
#.rfind() : string will be checked in reverse
#.capitalize() : first letter will be capitalized
#.upper() : all letters will be capitalized
#.lower() : all letters will be in small case
#.isdigit() : checks if the string is a number
#.isalpha() : checks if the string is an alphabet
#.count() : counts the number of times a substring appears in the string
#for example, if we want to count the number of times "a" appears in the name, we can use:
#a_count = name.count("a")
#.replace() : replaces a substring with another substring
#for example, if we want to replace all occurrences of "a" with "o", we can use:
#new_name = name.replace("a", "o")

#Baki ki jankari ke liye 
#print(help(str))
#run kar diyo