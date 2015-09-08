import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)
from player import *
from ship import *
from game import *

class TestGame(unittest.TestCase):

  def test_game_has_two_players_on_creation(self):
    self.game = Game()
    self.assertEqual(len(self.game.players), 2)


if __name__ == '__main__':
  unittest.main()