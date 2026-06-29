# ----------arena_simulator.py----------
# module = A file containing code you want to include in your program.
#          Use 'import' to include a module (built-in or your own)
#          Useful to break up a large program into reusable separate files 

import battle_engine

player_hp =  100
enemy_hp = 100

print("Welcome to the Arena!")

while player_hp > 0 and enemy_hp > 0:

    print("\nYour HP:", player_hp)
    print("Enemy HP:", enemy_hp)

    choice = input("\n Attack or heal? (a/h): ").lower()

    if choice == 'a':
        damage = battle_engine.attack()

        if battle_engine.critical_hit():
            damage *= 2
            print(f"Critical hit! you dealt {damage} damage!")
        else:
            print(f"You dealt {damage} damage.")

        enemy_hp -= damage

    elif choice == 'h':
        healing = battle_engine.heal()
        player_hp += healing

        if player_hp > 100:
            player_hp = 100

        print(f"You healed for {healing} HP.")

    else:
        print("Invalid choice. Please choose 'a' to attack or 'h' to heal.")
        continue

    if enemy_hp > 0:
        enemy_damage = battle_engine.enemy_attack()
        player_hp -= enemy_damage
        print(f"The enemy attacks and deals {enemy_damage} damage!")

print()

if player_hp > 0:
    print("Congratulations! You won the battle!")
else:
    print("You have been defeated!")