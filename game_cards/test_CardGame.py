from unittest import TestCase
from CardGame import CardGame


class TestCardGame(TestCase):
    # Set a global object of the class for the tests
    def setUp(self):
        # CardGame object that the number of cards is default
        self.cardgame = CardGame("Raz", "Itamar")
        # CardGame object that the number of cards is 10
        self.cardgame_10_cards = CardGame("Raz", "Itamar", 10)

    # Test a common way to start the game when number of cards set to default
    def test__init__valid_26_cards(self):
        self.assertTrue(self.cardgame.player1.name == "Raz")
        self.assertTrue(self.cardgame.player2.name == "Itamar")
        self.assertTrue(self.cardgame.num_of_cards == 26)
        # check if it is possible to start a new game after game object is created
        self.assertIs(self.cardgame.start_game, False)

    # Test a common way to start the game when number of cards set to 10
    def test__init__valid_10_cards(self):
        self.assertTrue(self.cardgame_10_cards.player1.name == "Raz")
        self.assertTrue(self.cardgame_10_cards.player2.name == "Itamar")
        self.assertTrue(self.cardgame_10_cards.num_of_cards == 10)
        self.assertIs(self.cardgame_10_cards.start_game, False)
        # The method automatically call to the new_game method, so as we create new game object
        # the cards in the deck will move to the players hand's
        # if the number of cards for each player is less than 26 then some cards will remain in the deck
        self.assertEqual(len(self.cardgame_10_cards.deck.deck), 32)

    # Test the init method whit invalid end values for number of cards
    def test__init__invalid_end_values(self):
        invalid_high_value = CardGame("Raz", "Itamar", 27)
        self.assertTrue(invalid_high_value.num_of_cards == 26)
        invalid_low_value = CardGame("Raz", "Itamar", 9)
        self.assertTrue(invalid_low_value.num_of_cards == 26)

    # Test the init method whit invalid types for players name and number of card
    def test__init__invalid_types(self):
        with self.assertRaises(TypeError):
            self.invalid_player1_name = CardGame(12, "Itamar", 26)
        with self.assertRaises(TypeError):
            self.invalid_player2_name = CardGame("Raz", 12, 26)
        with self.assertRaises(TypeError):
            self.invalid_number_of_card = CardGame("Raz", "Itamar", "26")

    # Test the new_game method when start game = True
    def test_new_game_valid(self):
        self.assertEqual(len(self.cardgame.player1.cards), 26)
        self.assertEqual(len(self.cardgame.player2.cards), 26)
        self.assertEqual(len(self.cardgame.deck.deck), 0)
        self.assertTrue(self.cardgame.start_game is False)

    # Try to call the method not from init
    def test_new_game_call_not_from_init(self):
        self.cardgame_10_cards.new_game()
        self.assertEqual(len(self.cardgame_10_cards.player1.cards), 10)
        self.assertEqual(len(self.cardgame_10_cards.player2.cards), 10)
        self.assertEqual(len(self.cardgame_10_cards.deck.deck), 32)

    # Test a case when player1 is the winner
    def test_get_winner_player1(self):
        self.cardgame.player2.cards.pop(0)
        self.assertTrue(self.cardgame.get_winner() == self.cardgame.player1)

    # Test a case when player2 is the winner
    def test_get_winner_player2(self):
        self.cardgame.player1.cards.pop(0)
        self.assertTrue(self.cardgame.get_winner() == self.cardgame.player2)

    # Test a case when there's a Tie
    def test_get_winner_tie(self):
        self.assertIs(self.cardgame.get_winner(), None)
