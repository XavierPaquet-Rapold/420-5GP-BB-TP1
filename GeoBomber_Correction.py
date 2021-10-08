# Geo Bomber - version à corriger

import random
import os
from pathlib import Path


def main():
    with open(os.path.join(os.getcwd(), 'liste-197-etats-2020.csv')) as country_file:
        file_contents = country_file.readlines()

    del file_contents[0]

    countries = {}

    for country_line in file_contents:
        fields = country_line.split(';')
        country = fields[0]
        capital = fields[-1]
        countries[country] = capital.rstrip('\n')

    name = input("Bienvenue démineur. Quel est ton nom? ")

    print(f"{name}, quel nom ridicule pour un dénomineur! Enfin, allons-y quand même...")

    retry_game = ""
    while retry_game != 'n':

        number_of_bomb = random.randint(1, 4)    # nombre de bombes

        bomb = [[" " for _ in range(2)] for _ in range(5)]
        for i in range(len(bomb)):
            bomb[i][0], bomb[i][1] = random.choice(list(countries.items()))

        # Sélection des bons fils
        wire_good_selection = []
        for i in range(number_of_bomb):
            index = random.randint(0, 4)
            while index in wire_good_selection:
                index = random.randint(0, 4)
            wire_good_selection.append(index)

             #s'assurer que le pays a une autre capital que la tienne
            random_choice = random.choice(list(countries.values()))
            while random_choice != bomb[i][1]:
                bomb[i][1] = random_choice
            else:
                random_choice = random.choice(list(countries.values()))
            
        print(f"Voici une bombe pour toi, {name}...")

        wire_cutted = []
        end_game_lose = False
        end_game_win = False
        cutted_wire = 0
        while not end_game_lose and not end_game_win:

            for i in range(len(bomb)):
                if i in wire_cutted:
                    print(f"[{i + 1:2d}] {bomb[i][0]} ~~/ /~~ {bomb[i][1]}")
                else:
                    print(f"[{i + 1:2d}] {bomb[i][0]} ~~~~~~~ {bomb[i][1]}")

            wire = input('\n' + "Quel câble veux-tu couper? ")
            
            if wire in ['1', '2', '3', '4', '5']:
                for i in range(len(bomb)):
                    if int(wire) == i + 1 :
                        if bomb[i][1] != countries[bomb[i][0]]:
                            end_game_lose = False
                            cutted_wire += 1
                            wire_cutted.append(i)
                        else:
                            end_game_lose = True

                if end_game_lose == False and cutted_wire == number_of_bomb:
                    end_game_win = True

            else : 
                print("ce fil n'existe pas...")

        if end_game_lose:
            print("*** BOOM! ***")
        elif end_game_win:
            print(f"OMG!!! Bombe désamorçée. Bravo {name}!")

        while retry_game != 'y' and retry_game != 'n':
            retry_game = input("Voulez-vous rejouer? (y/n)")

if __name__ == "__main__":
    main()
