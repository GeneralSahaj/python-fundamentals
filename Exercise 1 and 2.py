# Exercise 1 Rectangle Area Calculation
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")

# Exercise 2 Shppping Cart Program

item = input("Enter the name of the item: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
total_cost = price * quantity

print(f"You have added {quantity} {item}(s) to your cart.")
print(f"Your total cost is: ${total_cost:}")