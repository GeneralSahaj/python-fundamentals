# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# print or assign one of two values based on a condition
# formula: X if condition else Y

print("Welcome to Gamer Life Advisor. Making bad decisions faster since 2026.")
print()

q1 = input("Do you have assignments due? (yes/no): ")

print()

print( "And yet you opened a game first. Bold strategy." if q1.lower() == "yes" else "Free time detected. Miracles do happen.")

print()

q2 = input("Are your friends online? (yes/no): ")

print()

print("Your productivity is officially gone." if q2.lower() == "yes" else "Even your teammates abandoned you for studying.")

print()

q3 = input("“Did you already promise yourself just one match? (yes/no): ")

print()

print("See you in 6 hours." if q3.lower() == "yes" else "Impressive self-control. Probably temporary though.")

print()

final = ("Please go touch your assignments before touching ranked mode." if q1.lower() == "yes" else "Gaming session approved.")

print("Final verdict: ", end="")

print(final)