# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                Two ways to achieve polymorphism
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck Typing" = Object must have necessary attributes/methods


from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
        
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

shapes = [Circle(4), Square(5), Triangle(6, 7)]

for shape in shapes:
    print(shape.area())



# Basically Shape mainly provides structure, organization, and enforcement, not functionality.
# remove the shape class and suddenly we are duck typing 
# Big waste of time but something learned nonetheless