# Number Guessing Game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print ("Welcome to".center(30))
print ("THE NUMBER GUESSING GAME".center(30))
print()
print (f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    
    guess = input("Enter a number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1


        if guess < lowest_num or guess > highest_num:
            print("The number is out of range")
            print (f"please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low! Try Again!")
        elif guess > answer:
            print("Too High! Try Again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    
    else:
        print("Invalid Guess")
        print (f"Please select a number between {lowest_num} and {highest_num}")