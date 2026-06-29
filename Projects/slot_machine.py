#Python Slot Machine
import random

def spin_row():
    symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍋":
            return bet * 3
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "💎":
            return bet * 10
        elif row[0] == "7️⃣":
            return bet * 25
        
    return 0 


def main():
    balance = 100.0
    print("****************************")
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒 🍋 🔔 💎 7️⃣")     
    print("****************************")

    while balance > 0:
        print(f"Current Balance: ${balance:.2f}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input. Please enter a numeric value for the bet.")
            continue

        bet = int(bet)

        if bet > balance:
            print("You cannot bet more than your current balance.")
            continue

        if bet <= 0:
            print("Bet amount must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Congratulations you won : {payout}")
        else:
            print("Better Luck Next Time")

        balance += payout

        play_again = input("Do you want to Test Your Luck Again? (Y/N): ").upper()

        if play_again != "Y":
            break
    print("****************************************************************")
    print("The jackpot grows restless... come back to test your luck again!")
    print(f"Your Final Balance is: {balance}")
    print("****************************************************************")

if __name__ == "__main__":
    main()