# Geo Bomber - version corrigée

import random
import os
from pathlib import Path

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'liste-197-etats-2020.csv'), 'r', encoding='Latin-1') as country_file:
    file_content = country_file.readlines()

#supprimer la première ligne, car ce sont les titres de chaque colonne
del file_content[0]

countries = {}

for country_line in file_content:
    fields = country_line.split(';')
    country = fields[0]
    capital = fields[-1]
    countries[country] = capital.rstrip('\n')

name = input("Bienvenue démineur. Quel est ton nom? ")

print(f"{name}, quel nom ridicule pour un dénomineur! Enfin, allons-y quand même...")

round_status = 0
while round_status != 'n':

    nb_bad_associations = random.randint(1, 4)    # nombre de bombes

    bomb = [[" " for _ in range(2)] for _ in range(5)]
    for i in range(5):
        bomb[i][0], bomb[i][1] = random.choice(list(countries.items()))

    # Sélection des bons fils
    index_bad_associations = []
    for _ in range(nb_bad_associations):
        index = random.randint(0, 4)
        while index in index_bad_associations:
            index = random.randint(0, 4)
        index_bad_associations.append(index)

    for i in index_bad_associations:
        country_capital_mismatch = True
        while country_capital_mismatch:
            capital = random.choice(list(countries.values()))
            if capital != bomb[i][1]:
                bomb[i][1] = capital
                country_capital_mismatch = False

    print(f"Voici une bombe pour toi, {name}...")

    wire_cut = []

    game_status = 0
    nb_wire_cut = 0
    while not game_status:

        for i in range(5):
            if i in wire_cut:
                print(f"[{i + 1:2d}] {bomb[i][0]} ~~/ /~~ {bomb[i][1]}")
            else:
                print(f"[{i + 1:2d}] {bomb[i][0]} ~~~~~~~ {bomb[i][1]}")

        print()
        print("Quel câble veux-tu couper? ", end='')
        wire = input()
        if wire in ['1', '2', '3', '4', '5']:
            if wire == '1':
                if bomb[0][1] != countries[bomb[0][0]]:
                    game_status = 1
                    if 0 not in wire_cut:
                        nb_wire_cut += 1
                    wire_cut.append(0)
                else:
                    game_status = 3
            if wire == '2':
                if bomb[1][1] != countries[bomb[1][0]]:
                    game_status = 1
                    if 1 not in wire_cut:
                        nb_wire_cut += 1
                    wire_cut.append(1)
                else:
                    game_status = 3
            if wire == '3':
                if bomb[2][1] != countries[bomb[2][0]]:
                    game_status = 1
                    if 2 not in wire_cut:
                        nb_wire_cut += 1
                    wire_cut.append(2)
                else:
                    game_status = 3
            if wire == '4':
                if bomb[3][1] != countries[bomb[3][0]]:
                    game_status = 1
                    if 3 not in wire_cut:
                        nb_wire_cut += 1
                    wire_cut.append(3)
                else:
                    game_status = 3
            if wire == '5':
                if bomb[4][1] != countries[bomb[4][0]]:
                    game_status = 1
                    if 4 not in wire_cut:
                        nb_wire_cut += 1
                    wire_cut.append(4)
                else:
                    game_status = 3

            if game_status == 1 and nb_wire_cut == nb_bad_associations:
                game_status = 2

            game_status = game_status - 1

    if game_status == 2:
        print("*** BOOM! ***")
    else:
        print(f"OMG!!! Bombe désamorçée. Bravo {name}!")

    while round_status != 'y' and round_status != 'n':
        print(f"Voulez-vous rejouer? (y/n)", end=' ')
        round_status = input()
