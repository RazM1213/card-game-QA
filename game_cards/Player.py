from Card import Card
from DeckOfCards import DeckOfCards
import random


class Player:
    # Player constructor:
    def __init__(self, name: str, num_of_cards=26):
        if type(name) != str:
            raise TypeError("Name must be str type!")
        if type(num_of_cards) != int:
            raise TypeError("Number of cards must be an integer!S")
        if num_of_cards < 10 or num_of_cards > 26:
            num_of_cards = 26
        self.name = name
        self.num_of_cards = num_of_cards
        self.cards = []

    # return the name of the player
    def __str__(self):
        return f"{self.name}"

    # Used to hand out cards to the player out of the deck of cards:
    def set_hand(self, deck_of_cards: DeckOfCards):
        """
        This method gets DeckOfCards object as a parameter, and deals the player the amount of cards it has to get
        Each card is unique
        """
        if type(deck_of_cards) != DeckOfCards:
            raise TypeError("Deck of cards must be a DeckOfCards type!")
        if len(deck_of_cards.deck) < self.num_of_cards:
            raise ValueError("There's not enough cards in the deck to hand out to the player")
        for i in range(self.num_of_cards):
            card = deck_of_cards.deal_one()
            self.cards.append(card)

