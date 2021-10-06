# Geo Bomber - version à corriger

import random
import os
from pathlib import Path

country_file = open(os.path.join(os.getcwd(), 'liste-197-etats-2020.csv'))
file_contents = country_file.readlines()

del file_contents[0]

countries = {}

for line_country in file_contents:
    fields = line_country.split(';')
    countries[fields[0]] = fields[-1].rstrip('\n')

#print("Bienvenue démineur. Quel est ton nom? ", end='')
name = input("Bienvenue démineur. Quel est ton nom? ")

print(f"{name}, quel nom ridicule pour un dénomineur! Enfin, allons-y quand même...")

retry_game = 0
while retry_game != 'n':

    number_of_bomb = random.randint(1, 4)    # nombre de bombes

    bomb = [[" " for _ in range(2)] for _ in range(5)]
    for i in range(5):
        bomb[i][0], bomb[i][1] = random.choice(list(countries.items()))

    # Sélection des bons fils
    indexes = []
    for _ in range(number_of_bomb):
        index = random.randint(0, 4)
        while index in indexes:
            index = random.randint(0, 4)
        indexes.append(index)

    for i in indexes:
        bomb[i][1] = random.choice(list(countries.values()))

    print(f"Voici une bombe pour toi, {name}...")

    cut_wire = []
    end_game = 0
    n = 0
    while not end_game:

        for i in range(5):
            if i in cut_wire:
                print(f"[{i + 1:2d}] {bomb[i][0]} ~~/ /~~ {bomb[i][1]}")
            else:
                print(f"[{i + 1:2d}] {bomb[i][0]} ~~~~~~~ {bomb[i][1]}")

        print()
        print("Quel câble veux-tu couper? ", end='')
        fil = input()

        if fil in ['1', '2', '3', '4', '5']:
            if fil == '1':
                if bomb[0][1] != countries[bomb[0][0]]:
                    end_game = 1
                    n += 1
                    cut_wire.append(0)
                else:
                    end_game = 3
            if fil == '2':
                if bomb[1][1] != countries[bomb[1][0]]:
                    end_game = 1
                    n += 1
                    cut_wire.append(1)
                else:
                    end_game = 3
            if fil == '3':
                if bomb[2][1] != countries[bomb[2][0]]:
                    end_game = 1
                    n += 1
                    cut_wire.append(2)
                else:
                    end_game = 3
            if fil == '4':
                if bomb[3][1] != countries[bomb[3][0]]:
                    end_game = 1
                    n += 1
                    cut_wire.append(3)
                else:
                    end_game = 3
            if fil == '4':
                if bomb[4][1] != countries[bomb[4][0]]:
                    end_game = 1
                    n += 1
                    cut_wire.append(4)
                else:
                    end_game = 3

            if end_game == 1 and n == number_of_bomb:
                end_game = 2

            end_game = end_game - 1

    if end_game == 2:
        print("*** BOOM! ***")
    else:
        print(f"OMG!!! Bombe désamorçée. Bravo {name}!")

    while retry_game != 'y' and retry_game != 'n':
        print(f"Voulez-vous rejouer? (y/n)", end=' ')
        retry_game = input()