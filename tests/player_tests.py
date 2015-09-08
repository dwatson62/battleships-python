import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)
from player import *
from ship import *

class TestPlayer(unittest.TestCase):

  def setUp(self):
    self.player = Player()

  def test_player_exists(self):
    self.assertEqual(self.player, self.player)

  def test_player_starts_with_no_ships_placed(self):
    """
    On player creation, player has no ships on board
    """
    self.assertEqual(len(self.player.ships), 0)

  def test_player_can_place_a_sub(self):
    """
    Player can place a sub, and have record of its position
    """
    self.sub = Ship('Sub')
    self.player.place_ship(self.sub, 'A1')
    self.assertEqual(self.player.ships, [{'ship': 'Sub', 'position': 'A1'}] )

if __name__ == '__main__':
  unittest.main()