from unittest import TestCase
from DeckOfCards import DeckOfCards
from Card import Card


class TestDeckOfCards(TestCase):
    # Set a global object of the class for the tests
    def setUp(self):
        self.deck_of_cards = DeckOfCards()

    # Test the __init__ method, that the list contains 52 items, and that the items are not the same card
    def test__init__valid(self):
        self.assertTrue(len(self.deck_of_cards.deck) == 52)
        card_index = 0
        for suit in range(1, 5):
            for value in range(1, 14):
                card = Card(value, suit)
                self.assertEqual(card.value, self.deck_of_cards.deck[card_index].value)
                self.assertEqual(card.suit, self.deck_of_cards.deck[card_index].suit)
                card_index += 1

    # Test the valid option of the card shuffle method
    def test_card_shuffle_valid(self):
        shuffled_deck = DeckOfCards()
        shuffled_deck.card_shuffle()
        self.assertNotEqual(self.deck_of_cards.deck, shuffled_deck.deck)

        # Test the minimum value of cards amount in deck to shuffle
        self.deck_of_cards.deck = []
        self.deck_of_cards.deck.append(Card(1, 1))
        self.deck_of_cards.deck.append(Card(1, 2))
        DeckOfCards.card_shuffle(self.deck_of_cards)
        self.assertTrue(self.deck_of_cards)
        print(self.deck_of_cards.deck)

    # Test an invalid shuffle for deck (less than 2 cards)
    def test_card_shuffle_invalid(self):
        self.deck_of_cards.deck = []
        self.deck_of_cards.deck.append(Card(1, 1))
        with self.assertRaises(AttributeError):
            DeckOfCards.card_shuffle(self.deck_of_cards)

    # Test that when calling the method she return Card and remove it from the deck
    def test_deal_one_valid(self):
        self.assertTrue(type(self.deck_of_cards.deal_one()) == Card)
        self.assertEqual(len(self.deck_of_cards.deck), 51)

    # Test invalid case when the deck is empty
    def test_deal_one_invalid(self):
        self.deck_of_cards.deck = []
        with self.assertRaises(AttributeError):
            self.deck_of_cards.deal_one()
