class Meld:
    type= None
    cards = []
    def __init__(self, type, cards):
        # Check if input is valid Meld
        if type != "Run" and type != "Set":
            raise ValueError("Invalid Meld Type")
        if len(cards) < 3:
            raise ValueError("Invalid Meld Length")

        self.type = type
        self.cards = cards

        if not self.checkValidity():
            raise ValueError("Invalid Meld")
    
    def is_valid_meld(cards):
        if len(cards) < 3:
            return False

        # Check if all cards have the same number (set meld)
        if all(card.number == cards[0].number for card in cards[1:]):
            return "Set"

        # Check if all cards are of the same suit and form a sequence (run meld)
        if all(card.suit == cards[0].suit for card in cards[1:]) and \
           all(card.number == cards[i-1].number + 1 for i, card in enumerate(cards[1:], start=1)):
            return "Run"

        return False

    def add(self, card, pre):
        # Copy self for checking
        temp = Meld(self.type, self.cards.copy())
        if not pre:
            # Add to end
            temp.cards.append(card)
            return self
        else:
            # Add to beginning
            temp.cards.insert(0, card)

        if temp.checkValidity():
            self.cards = temp.cards
            return self
        else:
            return False
    
    def checkValidity(self):
        if self.type == "Run":
            return self.checkRun()
        elif self.type == "Set":
            return self.checkSet()
        else:
            return False
        
    def checkRun(self):
        color = self.cards[0].type
        if len(self.cards) < 3:
            return False
        for i in range(len(self.cards) - 1):
            if self.cards[i].number + 1 != self.cards[i + 1].number or self.cards[i].type != color:
                return False
        return True
    
    def checkSet(self):
        seenColors = []
        if len(self.cards) < 3:
            return False
        for i in range(len(self.cards) - 1):
            if self.cards[i].number != self.cards[i + 1].number:
                return False
            if self.cards[i].type in seenColors:
                return False
            seenColors.append(self.cards[i].type)
        return True
    
    def checkFullness(self):
        if self.type == "Set":
            return len(self.cards) == 4
        elif self.type == "Run":
            return False
        

