#Python Calculator

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")

elif operator == "-":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")

elif operator == "*":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")    

elif operator == "/":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator. Please enter one of +, -, *, or /.")

