import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)
from player import *
from ship import *
from game import *

class TestGame(unittest.TestCase):

  def setUp(self):
    self.game = Game()
    self.player1 = Player('Player1')
    self.player2 = Player('Player2')

  def test_displays_players_own_board(self):
    board = self.game.display_board(self.player1)
    self.assertEqual(len(board), 10)

  def test_displays_players_opponent_board(self):
    self.player1.place_ship(Ship('Destroyer'), 'J1')
    # self.player2.shoot(self.player1, 'J1')
    self.player2.shoot(self.player1, 'J9')
    board = self.game.display_board(self.player1, 'ME')
    for row in board:
      print row
    self.assertEqual(len(board), 10)

  def test_says_game_over(self):
    self.player1.place_ship(Ship('Sub'), 'J1')
    self.player2.place_ship(Ship('Sub'), 'J9')
    self.player1.shoot(self.player2, 'J9')
    self.assertEqual(self.game.declare_winner(self.player1, self.player2), 'Player 1 wins!' )

if __name__ == '__main__':
  unittest.main()