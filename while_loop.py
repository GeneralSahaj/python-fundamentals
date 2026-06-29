# While loop = execute some code WHILE a condition remains true

# fun little simulator

health = 100
medkit = 3
wave = 0

print("=== ZOMBIE SURVIVAL SIMULATOR ===")

while health > 0:
    print("\n-------------------")
    print(f"Health: {health}")
    print(f"Medkits: {medkit}")
    print(f"Wave: {wave}")

    choice = input("Do you want to (A)ttack, (H)eal, or (R)un? ").lower()

    if choice == "a":
        print("You attack the zombies!")
        health -= 20
        wave += 1

        # Random bonus every 3 waves
        if wave > 0 and wave % 3 == 0:
         print("You found a medkit!")
         medkit += 1

    elif choice == "h":
        if medkit > 0:
            print("You used a medkit!")
            health += 30
            medkit -= 1

            if health > 100:
                health = 100
        else:
            print("You don't have any medkits!")
    elif choice == "r":
        print("You ran away from the zombies!")
        health -= 10
    else:
        print("Invalid choice. Please try again.")

    
print("\nGame Over!")
print(f"You survived {wave} waves of zombies.")