from game.game import Game

print("Welcome to Holland Poker!")
print("How many players are there?")
players = int(input())
game = Game(players)

print("Let's play!")
print("Round 1: One triplicate")

game.deal()

for player in game.getPlayers():
    print(f"{player.name}: {player.getHand()}")
