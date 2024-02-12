class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def getHand(self):
        return self.hand
    
    def draw(self, deck):
        self.hand.append(deck.draw())
        return self
    
    def discard(self, card):
        self.hand.remove(card)
        return self
    
    def hit(self, card, pubishment_card1, pubishment_card2):
        self.hand.append(card)
        self.hand.append(pubishment_card1)
        self.hand.append(pubishment_card2)
        return self
    
    def discard(self, cards):
        for card in cards:
            self.hand.remove(card)
        return self