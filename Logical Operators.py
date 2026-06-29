# logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition is true
# and = all conditions must be true
# not = inverts the condition (not true = false, not false = true)

#Self made example which uses all 3 logical operators

# Mini decision helper

print("Mini Decision Helper".center(30))

answer1 = input("Do you feel tired? (yes/no): ")
answer2 = input("Do you feel stressed? (yes/no): ")

# OR operator

if answer1.lower() == "yes" or answer2.lower() == "yes":
    print("You may need a short break.")

    answer3 = input("Do you also have free time right now? (yes/no): ")

    # AND operator
    if answer1.lower() == "yes" and answer3.lower() == "yes":
        print("A quick nap or snack might help you feel better.")

        answer4 = input("But is the work you ignored while claiming to have free time very important? (yes/no): ")

        # NOT operator
        if not answer4.lower() == "yes":
            print("Enjoy your break! But don't forget to get back to work after.")
        else:
            print("Make sure to finish your important work before taking a break.")

    else:
        print("Maybe just stretch for a few minutes to refresh yourself.")

else:
    print("Great! Keep up the good work and remember to take breaks when needed.")