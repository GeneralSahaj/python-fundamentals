# Magic Method / Dunder Method (double underscore) like __init__, __str__, __eq__
# they are automatically called by many of python's built-in operations
# they allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    

    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, item):
        return item in self.title or item in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
        
book1 = Book("The Astonishing Color of After", "Emily X. R. Pan", 480)

book2 = Book("The Count of Monte Cristo", "Alexandre Dumas", 1276)

book3 = Book("The Song of Achilles", "Madeline Miller", 384)


print("\n========== LIBRARY SYSTEM ==========\n")

# __str__()
print("1. Displaying Book Information")
print(book1)
print(book2)
print(book3)

print("\n========== BOOK COMPARISON ==========\n")

# __eq__()
print("2. Checking if two books are the same")

duplicate_book = Book("The Song of Achilles", "Madeline Miller", 384)

print(book3 == duplicate_book)

print("\n========== BOOK SIZE COMPARISON ==========\n")

# __lt__()
print("3. Which book is shorter?")
print(book1 < book2)

# __gt__()
print("\n4. Which book is longer?")
print(book2 > book3)

print("\n========== READING CHALLENGE ==========\n")

# __add__()
print("5. Total pages if you read two books")
print(book1 + book3)

print("\n========== LIBRARY SEARCH ==========\n")

# __contains__()
print("6. Searching for keywords")

print("Achilles" in book3)
print("Dumas" in book2)
print("Harry Potter" in book1)

print("\n========== BOOK DATABASE ==========\n")

# __getitem__()
print("7. Accessing book details")

print(book1["title"])
print(book1["author"])
print(book1["num_pages"])

print("\n8. Looking for a missing field")
print(book1["publisher"])