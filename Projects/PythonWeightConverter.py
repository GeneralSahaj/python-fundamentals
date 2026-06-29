# Weight Converter

weight = float(input("Enter the weight: "))
unit = input("Enter the unit (K for kilograms, L for pounds): ")

if unit.upper() == "K":
    weight = weight * 2.20462
    unit  = "Lbs."
elif unit.upper() == "L":
    weight = weight * 0.453592
    unit = "Kgs."
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")

print(f"The weight is: {weight:.2f} {unit}")