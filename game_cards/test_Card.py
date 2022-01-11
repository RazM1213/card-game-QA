from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    # Instantiating objects of the tested class - Card:
    def setUp(self):
        self.ace_of_diamond = Card(1, 1)
        self.ace_of_club = Card(1, 4)
        self.king_of_club = Card(13, 4)
        self.ten_of_heart = Card(10, 3)

    # Checks that __init__ sets the correct attributes to the card object upon instantiation
    def test__init__valid(self):
        self.assertTrue(type(self.ace_of_diamond) == Card)
        self.assertEqual(self.ace_of_diamond.value, 1)  # Min value
        self.assertEqual(self.ace_of_diamond.suit, 1)  # Min suit
        self.assertEqual(self.king_of_club.value, 13)  # Max value
        self.assertEqual(self.king_of_club.suit, 4)  # Max suit

    # Check that error is raised if card value is not of type int
    def test__init__invalid_1(self):
        with self.assertRaises(TypeError):
            self.invalid_value_type_card = Card('test', 2)

    # Check that error is raised if card suit is not of type int
    def test__init__invalid_2(self):
        with self.assertRaises(TypeError):
            self.invalid_suit_type_card = Card(2, 'test')

    # Check that error is raised if card value is not between 1 and 13
    def test__init__invalid_3(self):
        with self.assertRaises(ValueError):
            self.invalid_value_range_card = Card(14, 2)

    # Check that error is raised if card value is not between 1 and 13
    def test__init__invalid_4(self):
        with self.assertRaises(ValueError):
            self.invalid_suit_range_card = Card(1, 5)

    # Checks that get_name method returns type str, the right card name representation
    def test_get_name_valid(self):
        self.assertEqual(self.ace_of_diamond.get_name(), 'Ace Of Diamond')

    # Checks that __gt__ method performs as expected
    def test__gt__valid(self):
        self.assertTrue(self.king_of_club > self.ten_of_heart)  # Comparing by value
        self.assertTrue(self.ace_of_club > self.ace_of_diamond)  # Comparing by suit
        self.assertTrue(self.ace_of_diamond > self.king_of_club)  # Ace is the strongest card
        self.assertFalse(self.ten_of_heart > self.king_of_club)  # False expression

    # Checks that TypeError is raised when comparing Card type object to other type object
    def test__gt__invalid_1(self):
        with self.assertRaises(TypeError):
            self.ace_of_diamond.__gt__(5)

    # Checks that ValueError is raised when comparing a card to itself
    def test__gt__invalid_2(self):
        with self.assertRaises(ValueError):
            self.king_of_club.__gt__(self.king_of_club)