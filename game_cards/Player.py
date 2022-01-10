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
