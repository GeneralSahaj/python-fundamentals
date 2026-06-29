import math

#Exercise 1 : Calculate the circumference of a circle

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference:.2f}")

#Exercise 2 : Calculate the area of a circle

radius = float(input("Enter the radius of the circle for area calculation: "))

area = math.pi * radius ** 2

print(f"The area of the circle is: {area:.2f}")


#Exercise 3 : Finding hypotenuse of a right triangle

side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))

hypotenuse = math.sqrt(pow(side_a, 2) + pow(side_b, 2))

print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
