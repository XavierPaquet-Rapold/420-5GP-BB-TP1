# Geo Bomber - version à corriger

import random
from pathlib import Path


country_file = open(Path.home() / 'liste-197-etats-2020.csv')
file_contents = country_file.readlines()

del file_contents[0]

countries = {}

for line in file_contents:
    fields = line.split(';')
    countries[fields[0]] = fields[-1].rstrip('\n')

name = input("Bienvenue démineur. Quel est ton nom? ")

print(f"{name}, quel nom ridicule pour un dénomineur! Enfin, allons-y quand même...")

quit_choice = 0
while quit_choice != 'n':

    
    bomb_number = random.randint(1, 4)    # nombre de bombes

    bomb = [[" " for _ in range(2)] for _ in range(5)]
    for i in range(5):
        bomb[i][0], bomb[i][1] = random.choice(list(countries.items()))

    # Sélection des bons fils
    indexes = []
    for i in range(bomb_number):
        index = random.randint(0, 4)
        while index in indexes:
            index = random.randint(0, 4)
        indexes.append(index)

    for i in indexes:
        bomb[i][1] = random.choice(list(countries.values()))

    print(f"Voici une bombe pour toi, {name}...")

    fils_coupes = []

    fin = 0
    n = 0
    while not fin:

        for i in range(5):
            if i in fils_coupes:
                print(f"[{i + 1:2d}] {bomb[i][0]} ~~/ /~~ {bomb[i][1]}")
            else:
                print(f"[{i + 1:2d}] {bomb[i][0]} ~~~~~~~ {bomb[i][1]}")


        fil = input('\n' + "Quel câble veux-tu couper? ")

        if fil in ['1', '2', '3', '4', '5']:
            if fil == '1':
                if bomb[0][1] != countries[bomb[0][0]]:
                    fin = 1
                    n += 1
                    fils_coupes.append(0)
                else:
                    fin = 3
            if fil == '2':
                if bomb[1][1] != countries[bomb[1][0]]:
                    fin = 1
                    n += 1
                    fils_coupes.append(1)
                else:
                    fin = 3
            if fil == '3':
                if bomb[2][1] != countries[bomb[2][0]]:
                    fin = 1
                    n += 1
                    fils_coupes.append(2)
                else:
                    fin = 3
            if fil == '4':
                if bomb[3][1] != countries[bomb[3][0]]:
                    fin = 1
                    n += 1
                    fils_coupes.append(3)
                else:
                    fin = 3
            if fil == '4':
                if bomb[4][1] != countries[bomb[4][0]]:
                    fin = 1
                    n += 1
                    fils_coupes.append(4)
                else:
                    fin = 3

            if fin == 1 and n == bomb_number:
                fin = 2

            fin = fin - 1
        else:
            print("ce fil n'existe pas")

    if fin == 2:
        print("*** BOOM! ***")
    else:
        print(f"OMG!!! Bombe désamorçée. Bravo {name}!")

    while choice != 'y' and choice != 'n':
        print(f"Voulez-vous rejouer? (y/n)", end=' ')
        choice = input()