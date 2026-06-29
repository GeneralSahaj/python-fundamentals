# Duck typing : Another way to achieve polymorphism besides inheritance
#               Object must have the minimum necessary attributes/inheritance
#               "We don't care what the object is, only whether it has the method being called."
#                                              or more formally
#               "If it walks like a duck and quacks like a duck, treat it like a duck."


class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Robot:
    def speak(self):
        print("Beep Boop!")

# This class does NOT have a speak() method
class Car:
    pass

animals = [Dog(), Cat(), Robot()]

# Duck typing in action:
# Python calls speak() on each object.
# It doesn't check the object's class/type.
for animal in animals:
    animal.speak()

# Car doesn't have a speak() method, so Python
# raises an AttributeError when the loop reaches it.
# Uncomment the 4 lines below to see an error.

# animals.append(Car())

# for animal in animals:
#     animal.speak()