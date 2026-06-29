#if = do some code if a condition is true
#elif = do something else if the condition is false but another condition is true
#else do something else if the condition is false

age = int(input("How old are you? "))

if age >= 100:
    print("You are ancient.")

elif age >= 18:
    print("You are an adult.")

elif age < 0:
    print("You are not born yet.")

else:
    print("You are a child.")
