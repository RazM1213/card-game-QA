from Card import Card
import random


class DeckOfCards:
    # creating a deck of card with all the cards values of every suit
    def __init__(self):
        self.deck = []
        for suit in range(1, 5):
            for value in range(1, 14):
                self.deck.append(Card(value, suit))
                