# Dice Roller Program with ASCII Art

import random

# ==================================================
# UNICODE REFERENCE
# ==================================================
#
# ● = \u25CF
# ┌ = \u250C
# ─ = \u2500
# ┐ = \u2510
# │ = \u2502
# └ = \u2514
# ┘ = \u2518
#
# These Unicode characters are used to draw the dice.
#

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

# ==================================================
# HOW THE DICTIONARY WORKS
# ==================================================
#
# Each number is linked to a tuple containing
# the 5 rows needed to draw that dice face.
#
# Example:
#
# dice_art[1]
#
# returns:
#
# ┌─────────┐
# │         │
# │    ●    │
# │         │
# └─────────┘
#
# Think of every dice as a list of rows:
#
# row 0 -> ┌─────────┐
# row 1 -> │         │
# row 2 -> │    ●    │
# row 3 -> │         │
# row 4 -> └─────────┘
#

dice = []
total = 0

# ==================================================
# USER INPUT
# ==================================================
#
# Ask the user how many dice they want to roll.
#
# Example:
#
# How many dice?: 3
#

num_of_dice = int(input("How many dice?: "))

# ==================================================
# ROLL THE DICE
# ==================================================
#
# Generate one random number (1-6) for each dice
# and store it inside the dice list.
#
# Example:
#
# User wants 3 dice
#
# Roll 1 -> 4
# Roll 2 -> 1
# Roll 3 -> 6
#
# Result:
#
# dice = [4, 1, 6]
#

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# ==================================================
# PRINT THE DICE ART
# ==================================================
#
# Example:
#
# dice = [3, 5]
#
# Dice 3:
#
# ┌─────────┐
# │ ●       │
# │    ●    │
# │       ● │
# └─────────┘
#
# Dice 5:
#
# ┌─────────┐
# │ ●     ● │
# │    ●    │
# │ ●     ● │
# └─────────┘
#
# We want:
#
# ┌─────────┐┌─────────┐
# │ ●       ││ ●     ● │
# │    ●    ││    ●    │
# │       ● ││ ●     ● │
# └─────────┘└─────────┘
#
# NOT:
#
# ┌─────────┐
# │ ●       │
# │    ●    │
# │       ● │
# └─────────┘
#
# ┌─────────┐
# │ ●     ● │
# │    ●    │
# │ ●     ● │
# └─────────┘
#

for line in range(5):

    # ==========================================
    # OUTER LOOP
    # ==========================================
    #
    # Decides WHICH ROW of the dice artwork
    # is currently being printed.
    #
    # line = 0 -> top border
    # line = 1 -> second row
    # line = 2 -> middle row
    # line = 3 -> fourth row
    # line = 4 -> bottom border
    #
    # Think:
    #
    # "Which row am I printing right now?"
    #

    for die in dice:

        # ======================================
        # INNER LOOP
        # ======================================
        #
        # Decides WHICH DICE will print
        # the current row.
        #
        # Example:
        #
        # dice = [3, 5, 1]
        #
        # If line = 0:
        #
        # Print row 0 of Dice 3
        # Print row 0 of Dice 5
        # Print row 0 of Dice 1
        #
        # Result:
        #
        # ┌─────────┐┌─────────┐┌─────────┐
        #
        #
        # If line = 1:
        #
        # Print row 1 of Dice 3
        # Print row 1 of Dice 5
        # Print row 1 of Dice 1
        #
        # Result:
        #
        # │ ●       ││ ●     ● ││         │
        #
        #
        # Think:
        #
        # "For this row, print it on every dice."
        #
        # Outer loop moves DOWN the rows.
        # Inner loop moves ACROSS the dice.
        #

        print(dice_art.get(die)[line], end="")

    # After every dice has printed the current row,
    # move to the next line of the terminal.
    print()

# ==================================================
# CALCULATE TOTAL
# ==================================================
#
# Example:
#
# dice = [4, 1, 6]
#
# total = 0
#
# total = 0 + 4 = 4
# total = 4 + 1 = 5
# total = 5 + 6 = 11
#

for die in dice:
    total += die

# ==================================================
# DISPLAY TOTAL
# ==================================================

print(f"Total: {total}")

# ==================================================
# EXAMPLE RUN
# ==================================================
#
# How many dice?: 3
#
# ┌─────────┐┌─────────┐┌─────────┐
# │ ●     ● ││         ││ ●     ● │
# │         ││    ●    ││ ●     ● │
# │ ●     ● ││         ││ ●     ● │
# └─────────┘└─────────┘└─────────┘
#
# Total: 11
#
# QUICK SUMMARY
#
# 1. Ask user how many dice to roll.
# 2. Generate random dice values.
# 3. Store them in a list.
# 4. Print dice row-by-row.
# 5. Add all values together.
# 6. Display the total.
#
# Mental Model:
#
# Outer Loop -> Which row?
# Inner Loop -> Which dice?
#
# Outer moves DOWN.
# Inner moves ACROSS.
#
# That's how the dice appear side-by-side.