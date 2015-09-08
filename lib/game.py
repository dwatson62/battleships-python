from player import *

class Game(object):

  def declare_winner(self, player1, player2):
    for ship in player2.ships:
      if not 'SUNK' in ship['positions']: return
    return 'Player 1 wins!'
    for ship in player1.ships:
      if not 'SUNK' in ship['positions']: return
    return 'Player 2 wins!'