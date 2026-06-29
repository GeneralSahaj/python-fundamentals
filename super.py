# Parent class
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


# Child class (Inheritance)
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  # Call parent constructor
        self.radius = radius

    def describe(self):  # Method overriding
        super().describe()  # Call parent method
        print(f"It is a circle with radius {3.14 * self.radius * self.radius}cm^2")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):  # Method overriding
        super().describe()
        print(f"It is a square with area {self.width * self.width}cm^2")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):  # Method overriding
        super().describe()
        print(f"It is a triangle with area  of {self.width * self.height / 2}cm^2")


# Object creation
circle = Circle(color="Red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=5)

# Calls Circle.describe() -> Shape.describe() -> Circle-specific code
circle.describe()