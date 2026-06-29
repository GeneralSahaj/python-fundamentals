# Temperature Converter

unit = input("Enter the unit to convert from (C for Celsius, F for Fahrenheit): ")

if unit.upper() == "C":
    temp = float(input("Enter the temperature in Celsius: "))
    temp = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {temp:.1f} F")
elif unit.upper() == "F":
    temp = float(input("Enter the temperature in Fahrenheit: "))
    temp = (temp - 32) * 5/9
    print(f"The temperature in Celsius is: {temp:.1f} C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")