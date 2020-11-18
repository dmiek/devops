"""
Module to create the playing deck for the game.
"""


import random


def create_deck():
    """ Method to generate playing deck. """
    cardfaces = []
    suits = ["C", "D", "H", "S"]
    royals = ["A", "T", "J", "Q", "K"]
    deck = []

    for i in range(2, 10):
        cardfaces.append(str(i))

    for i in range(len(royals)):
        cardfaces.append(royals[i])

    for i in range(len(suits)):
        for j in range(len(cardfaces)):
            card = (cardfaces[j] + suits[i])
            deck.append(card)
    random.shuffle(deck)
    return deck
