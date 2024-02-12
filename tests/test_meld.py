import unittest
from game.Card import Card
from game.meld import Meld

class TestMeldMethods(unittest.TestCase):
    def setUp(self):
        self.run_meld = Meld("Run", [Card("Hearts", 1), Card("Hearts", 2), Card("Hearts", 3)])
        self.set_meld = Meld("Set", [Card("Hearts", 1), Card("Diamonds", 1), Card("Clubs", 1)])

    def test_checkRun(self):
        self.assertTrue(self.run_meld.checkRun())
        self.run_meld.cards.append(Card("Hearts", 5))
        self.assertFalse(self.run_meld.checkRun())

    def test_checkSet(self):
        self.assertTrue(self.set_meld.checkSet())
        self.set_meld.cards.append(Card("Spades", 2))
        self.assertFalse(self.set_meld.checkSet())

    
    def test_checkFullness(self):
        self.assertFalse(self.run_meld.checkFullness())
        self.run_meld.cards.append(Card("Hearts", 4))
        self.assertFalse(self.run_meld.checkFullness())

        self.assertFalse(self.set_meld.checkFullness())
        self.set_meld.cards.append(Card("Spades", 1))
        self.assertTrue(self.set_meld.checkFullness())

    def test_invalidMeldCreation(self):
        with self.assertRaises(ValueError):
            invalid_run_meld = Meld("Run", [Card("Hearts", 1), Card("Hearts", 3), Card("Hearts", 5)])

        with self.assertRaises(ValueError):
            invalid_set_meld = Meld("Set", [Card("Hearts", 1), Card("Diamonds", 2), Card("Clubs", 3)])

        with self.assertRaises(ValueError):
            invalid_meld = Meld("Run", [Card("Hearts", 1), Card("Hearts", 2)])

            
        with self.assertRaises(ValueError):
            invalid_meld = Meld("Set", [Card("Hearts", 1), Card("Hearts", 2)])

if __name__ == '__main__':
    unittest.main()