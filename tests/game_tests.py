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
    self.player1 = Player()
    self.player2 = Player()

  def test_says_game_over(self):
    self.player2.place_ship(Ship('Sub'), 'J9')
    self.player1.shoot(self.player2, 'J9')
    self.assertEqual(self.game.declare_winner(self.player1, self.player2), 'Player 1 wins!' )

if __name__ == '__main__':
  unittest.main()