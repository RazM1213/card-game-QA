from unittest import TestCase
from CardGame import CardGame


class TestCardGame(TestCase):
    # Set a global object of the class for the tests
    def setUp(self):
        self.cardgame = CardGame("Raz", "Itamar")

    # Test a common way to start the game
    def test__init__valid(self):
        self.assertTrue(self.cardgame.player1.name == "Raz")
        self.assertTrue(self.cardgame.player2.name == "Itamar")
        self.assertTrue(self.cardgame.num_of_cards == 26)
        self.assertIs(self.cardgame.start_game, False)

    # Test the init method whit valid end values for number of cards
    def test__init__valid_end_values(self):
        max_end_value = CardGame("Raz", "Itamar", 26)
        self.assertTrue(max_end_value.num_of_cards == 26)
        min_end_value = CardGame("Raz", "Itamar", 10)
        self.assertTrue(min_end_value.num_of_cards == 10)

    # Test the init method whit invalid end values for number of cards
    def test__init__invalid_end_values(self):
        invalid_high_value = CardGame("Raz", "Itamar", 27)
        self.assertTrue(invalid_high_value.num_of_cards == 26)
        invalid_low_value = CardGame("Raz", "Itamar", 9)
        self.assertTrue(invalid_low_value.num_of_cards == 26)

    # Test the init method whit invalid types for players name and number of card
    def test__init__invalid_types(self):
        with self.assertRaises(TypeError):
            invalid_player1_name = CardGame(12, "Itamar", 26)
        with self.assertRaises(TypeError):
            invalid_player2_name = CardGame("Raz", 12, 26)
        with self.assertRaises(TypeError):
            invalid_number_of_card = CardGame("Raz", "Itamar", "26")

    def test_new_game(self):
        self.fail()

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
