import random
from game.Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.pile = []
    
    def build(self):
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))#
                self.shuffle
    
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw(self):
        # If the deck is empty, put the shuffled pile back into the deck
        if len(self.cards) == 0:
            self.PileToDeck()
        return self.cards.pop()
    
    def discard(self, card):
        self.pile.append(card)
        return self
    
    def getTopCard(self):
        return self.pile[-1]
    
    def PileToDeck(self):
        # Catch the top card
        top = self.pile.pop()
        self.cards.extend(self.pile)
        self.pile.clear()
        self.shuffle()
        # Put the top card back
        self.pile.append(top)
        return self
    