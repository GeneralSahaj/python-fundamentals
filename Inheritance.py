# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code resuability and extensibility
#               Class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleeping(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!!!")

class Cat(Animal):
    def speak(self):
        print("MEOW!!!")


dog = Dog("Muffin")
cat = Cat("Billu")

dog.speak()
cat.speak()

print(f"Name of the dog is {dog.name}")
print(f"Name of the cat is {cat.name}")
