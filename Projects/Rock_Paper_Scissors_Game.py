# Rock, Paper, Scissors Game
import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player =  input("Enter a choice (rock, paper, scissors): ").lower()


    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a TIE!")
    elif player == "rock" and computer == "scissors":
        print("You WIN!!!")
    elif player == "paper" and computer == "rock":
        print("You WIN!!!")
    elif player == "scissors" and computer == "paper":
        print("You WIN!!!")
    else:
        print("You LOSE!!!")

    if not input("Play Again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing")