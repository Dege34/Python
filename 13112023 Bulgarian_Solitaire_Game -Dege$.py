# Copyright © 2023 Dogan Ege BULTE
# https://github.com/Dege34
# dege.bulte@studenti.polito.it
# www.thedege.com

import random

def generate_initial_setup(card):
    piles = []

    while card > 0:
        pile_size = random.randint(1, card)
        piles.append(pile_size)
        card -= pile_size

    return piles

def bulgarian_gameplay(piles):
    while sorted(piles) != list(range(1, len(piles) + 1)):
        new_pile = len(piles)

        for i in range(len(piles)):
            piles[i] -= 1

        piles.append(new_pile)
        piles = [pile for pile in piles if pile > 0]

        print("Current setup:", piles)

    print("Final solitaire setup:", piles)

num_cards = 45
initial_setup = generate_initial_setup(num_cards)

print("Initial setup:", initial_setup)
bulgarian_gameplay(initial_setup)
