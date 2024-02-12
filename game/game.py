from game.Card import Card
from game.Deck import Deck
from game.Player import Player

class Game:
    players = []
    deck = None
    table = []
    round = 0
    turn = 0

    def __init__(self, players):
        # Create Players
        if players < 2:
            raise ValueError("Too few players")
        elif players < 5:
            for i in range(players):
                self.players.append(Player(f"Player {i + 1}"))
        else:
            # ERROR
            raise ValueError("Too many players")
        # Create Deck   
        self.deck = Deck()

    def playRound(self):
        self.deal()
        # Draw top card from deck and add to pile
        self.deck.discard(self.deck.draw())

    def getPlayers(self):
        return self.players
    
    def deal(self):
        for i in range(12):
            for player in self.players:
                player.draw(self.deck)

    
