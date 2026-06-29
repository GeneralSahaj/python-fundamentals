import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data ({response.status_code})")
        return None

pokemon_name = input("Enter Pokémon name: ").lower()

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:

    print("\n==========================")
    print("        POKEDEX")
    print("==========================")

    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: #{pokemon_info['id']}")

    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")

    print("\nTypes:")
    for pokemon_type in pokemon_info["types"]:
        print(f"- {pokemon_type['type']['name'].capitalize()}")

    print("\nAbilities:")
    for ability in pokemon_info["abilities"]:
        print(f"- {ability['ability']['name'].capitalize()}")

    print("\nBase Stats:")
    for stat in pokemon_info["stats"]:
        print(f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}")

    print("\n==========================")