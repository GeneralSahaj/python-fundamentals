# python compound_interest_calculator

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal amount cannot be negative. Please try again.")
    else:
        break

while True:
    rate = float(input("Enter the annual interest rate (in %): "))
    if rate < 0:
        print("Interest rate cannot be negative. Please try again.")
    else:
        break

while True:
    time = float(input("Enter the time (in years): "))
    if time < 0:
        print("Time cannot be negative. Please try again.")
    else:
        break

# Calculate compound interest
amount = principal * (1 + rate/100) ** time
compound_interest = amount - principal

# Display the result
print(f"\nThe compound interest is: ${compound_interest:.2f}")
print(f"The total amount after {time} years is: ${amount:.2f}")

