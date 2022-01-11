from Card import Card
import random


class DeckOfCards:
    # creating a deck of card with all the cards values of every suit
    def __init__(self):
        self.deck = []
        for suit in range(1, 5):
            for value in range(1, 14):
                self.deck.append(Card(value, suit))

    def __repr__(self):
        return f"{self.deck}"

    # A method that shuffles the cards randomly in the cards deck
    def card_shuffle(self):
        """shuffle the cards"""
        if len(self.deck) < 2:
            raise AttributeError("Can't shuffle when there's less than 2 cards!")
        random.shuffle(self.deck)

    # Pick one cards from the deck
    def deal_one(self):
        """picking random card from the deck"""
        if len(self.deck) == 0:
            raise AttributeError("Cant pick card from empty deck!")
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
