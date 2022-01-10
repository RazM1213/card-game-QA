class Card:
    # Card's constructor:
    def __init__(self, value, suit):
        if type(value) != int:
            raise TypeError("value must be int !")
        if type(suit) != int:
            raise TypeError("suit must be int !")
        if value > 13 or value < 1:
            raise ValueError("value must be in range 1-13 !")
        if suit > 4 or suit < 1:
            raise ValueError("suit must be in range 1-4 !")
        self.value = value
        self.suit = suit
