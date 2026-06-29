# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item you want to add to your cart (or type 'done' to finish): ")
    if food.lower() == 'done':
        break

    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)


print("------ Your Shopping Cart -----")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Total Price: ₹{total:.2f}")