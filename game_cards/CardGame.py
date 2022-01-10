from DeckOfCards import DeckOfCards
from Player import Player


class CardGame:
    # Class constructor
    def __init__(self, player1: str, player2: str, num_of_cards=26):
        """
        This __init__ method, instantiates 2 Player objects and invokes the new_game method
        to start a new game at CardGame object creation !
        """
        if type(player1) != str or type(player2) != str:
            raise TypeError("Name must be str type!")
        if type(num_of_cards) != int:
            raise TypeError("Number of cards must be an integer!S")
        if num_of_cards < 10 or num_of_cards > 26:
            raise ValueError("Number of cards must be in range 10-26")
        self.player1 = Player(player1, num_of_cards)
        self.player2 = Player(player2, num_of_cards)
        self.num_of_cards = num_of_cards
        # Call the new_game method, and create a variable to activate the method only from __init__
        self.start_game = True
        self.new_game()