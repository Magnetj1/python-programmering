import pokemon
import random

def calculate_damage(atk_type, def_type, attack, defence):
    effect = 1

    if atk_type == "fire" and def_type == "water":
        effect = 0.5
    if atk_type == "water" and def_type == "fire":
        effect = 2
    if atk_type == "grass" and def_type == "fire":
        effect = 0.5
    if atk_type == "fire" and def_type == "grass":
        effect = 2
    if atk_type == "water" and def_type == "grass":
        effect = 0.5
    if atk_type == "grass" and def_type == "water":
        effect = 2
    if atk_type == "water" and def_type == "electric":
        effect = 0.5
    if atk_type == "electric" and def_type == "water":
        effect = 2
    

    dmg = 50 * (attack/defence) * effect
    return dmg

# name, element, attack, defence, health
pikachu = pokemon.Pokemon("Pikachu", "electric", 100, 70, 200)
squirtle = pokemon.Pokemon("Squirtle", "water", 80, 100, 180)

choice = []
choice.append(pikachu)
choice.append(squirtle)

print("Välj din Pokémon")

for i in range(len(choice)):
    print(i, choice[i].name)

player_choice = int(input())

player_pokemon = choice[player_choice]
computer_pokemon = random.choice(choice)

damage_taken = calculate_damage(player_pokemon.element, computer_pokemon.element, player_pokemon.attack, computer_pokemon.defence)

print(player_pokemon.name, "dealt", round(damage_taken, 2), "to", computer_pokemon.name)