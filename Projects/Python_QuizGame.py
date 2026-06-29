# Python Quiz Game

questions = (
    "What is the process by which plants convert sunlight to energy? : ",
    "Which planet has the most moons? : ",
    "Where is the strongest human muscle located? : ",
    "What is the outermost layer of the Earth’s atmosphere called? : ")

options = (
    ("A. Resiration", "B. Photosynthesis", "C. Fermentation", "D. Digestion"),
    ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
    ("A. Arm", "B. Leg", "C. Jaw", "D. Back"),
    ("A. Troposphere", "B. Stratosphere", "C. Mesosphere", "D. Exosphere"))

answers = ("B", "C", "C", "D")

guesses = []

score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1


print("----------------------------------")
print("             RESULTS              ")
print("----------------------------------")

print("Answers: ",end="")
for answer in answers:
    print(answer, end="")
print()


print("Guesses: ",end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print (f"Your Score is {score}%")

if score == 100:
    print("NERD!!!!")

elif score <= 0:
    print("Tumse na ho payega, Tum rehne do")