import unittest
import pytest


from idioten_deck import create_deck

class TestNewDeck(unittest.TestCase):

    def test_createDeck_allowed_colour(self):
        # Check that deck only contains allowed colours.
        deck = create_deck()
        allowed_colour = ["D","S","C","H"]
        for i in deck:
            self.assertIn(i[1], allowed_colour)

    def test_createDeck_allowed_ranks(self):
        # Check that deck contains only allowed ranks.
        deck = createDeck()
        allowed_ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
        for i in deck:
            self.assertIn(i[0], allowed_ranks)

if __name__ == '__main__':
    unittest.main()
