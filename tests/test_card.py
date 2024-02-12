import unittest
from game.Card import Card
from game.meld import Meld

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", 1)

    def test_init(self):
        self.assertEqual(self.card.type, "Hearts")
        self.assertEqual(self.card.number, 1)

if __name__ == '__main__':
    unittest.main()