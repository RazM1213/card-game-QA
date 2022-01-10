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

    # A method to convert the card object attributes to text - for the card representation to be user-friendly
    def get_name(self):
        """
        The method uses two dictionaries - to create the string representation of the card.
        One is for the card value
        The second is for the card suit
        """
        value_dict = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

        suit_dict = {
            1: "Diamond",
            2: "Spade",
            3: "Heart",
            4: "Club"
        }
        return f"{value_dict[self.value]} Of {suit_dict[self.suit]}"
