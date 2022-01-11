from unittest import TestCase, mock
from unittest.mock import patch
from Player import Player
from Card import Card
from DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.deck_of_cards = DeckOfCards()
        self.player1 = Player("Raz", 10)
        self.player2 = Player("Itamar", 10)
        self.player3 = Player("Beni", 4)
        self.player4 = Player("Dani", 30)
        self.player5 = Player("Dan")

    # Checks __init__ method valid functionality
    def test__init__valid(self):
        self.assertEqual(self.player1.name, "Raz")  # Player gets expected name
        self.assertEqual(self.player1.num_of_cards, 10)  # Player gets expected num_of_cards
        self.assertEqual(self.player1.cards, [])  # A Player starts with an empty hand upon creation

        self.assertTrue(self.player3.num_of_cards == 26)  # Not enough cards - resets to 26
        self.assertTrue(self.player4.num_of_cards == 26)  # Too many cards - resets to 26

        self.assertTrue(self.player5.num_of_cards == 26)  # Gets default num of cards - 26

    # Checks that error is raised when name is not of type str
    def test__init__invalid_name_type(self):
        with self.assertRaises(TypeError):
            self.invalid_name_type_player = Player(2, 10)

    # Checks that error is raised when num_of_cards is not of type int
    def test__init__invalid_num_of_cards_type(self):
        with self.assertRaises(TypeError):
            self.invalid_num_of_cards_type_player = Player('test', 'invalid')

    # Checks that the dealt card from the deck is in Player's hand
    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=Card(10, 3))
    def test_set_hand_valid_card(self, mock_deal_one):
        self.player1.set_hand(self.deck_of_cards)
        self.assertIn(self.deck_of_cards.deal_one(), self.player1.cards)  # Check that the dealt card is in Player's hand

    # Checks that the player gets the amount of cards he has to get from the deck, according to num_of_cards attribute
    def test_set_hand_valid_num_of_cards(self):
        self.player1.set_hand(self.deck_of_cards)
        self.assertEqual(len(self.player1.cards), self.player1.num_of_cards)

    # Checks that set_hand method raises TypeError when it gets a parameter not of type DeckOfCards
    def test_set_hand_invalid_deck_type(self):
        with self.assertRaises(TypeError):
            self.player2.set_hand('deck')

    # Checks that ValueError is raised when trying to set hand bigger than the used deck
    def test_set_hand_invalid_deck_len(self):
        self.deck_of_cards.deck = []
        with self.assertRaises(ValueError):
            self.player3.set_hand(self.deck_of_cards)

    # Checks get_card method expected behaviour
    def test_get_card_valid(self):
        # Set the player's hand
        self.player1.set_hand(self.deck_of_cards)

        self.assertIsInstance(self.player1.get_card(), Card)  # Checks that get_card method returns a Card object
        self.assertEqual(len(self.player1.cards), self.player1.num_of_cards - 1)  # Checks if get_card method takes out one card from Player's hand

    # Checks that get_card method raises AttributeError if Player has no cards
    def test_get_card_invalid(self):
        with self.assertRaises(AttributeError):
            self.player1.get_card()

    # Checks that add_card adds the desired card to player's hand
    def test_add_card_valid(self):
        card = Card(1, 4)
        self.player1.add_card(card)
        self.assertEqual(self.player1.cards, [card])

    # Checks that add_card raises TypeError if it gets parameter of other type than Card
    def test_add_card_invalid(self):
        with self.assertRaises(TypeError):
            self.player1.add_card('test')
            
