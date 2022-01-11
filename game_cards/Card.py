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

    def __repr__(self):
        return self.get_name()

    # This method instructs python how to evaluate 2 different card objects
    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        return False

    # This method used to compare two cards objects:
    def __gt__(self, card):
        """
        Cards are compared by their value - higher value = stronger card
        If the compared cards share the same value - the comparison will be based on their suits
        Ace is the strongest card in the game - it's value is the highest amongst cards
        """
        if type(card) != Card:
            raise TypeError("card type must be of Card !")
        
        if self.value > card.value != 1:
            return True
        elif self.value == card.value:
            if self.suit > card.suit:
                return True
        elif self.value == 1 and card.value != 1:
            return True
        return False