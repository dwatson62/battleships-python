import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)
from player import *
from ship import *

class TestPlayer(unittest.TestCase):

  def setUp(self):
    self.player1 = Player()
    self.player2 = Player()

  def test_player_exists(self):
    self.assertEqual(self.player1, self.player1)

  def test_player_starts_with_no_ships_placed(self):
    """
    On player creation, player has no ships on board
    """
    self.assertEqual(len(self.player1.ships), 0)

  def test_player_can_place_a_sub(self):
    """
    Player can place a sub, and have record of its position
    """
    self.sub = Ship('Sub')
    self.player1.place_ship(self.sub, 'A1')
    self.assertEqual(self.player1.ships, [{'ship': 'Sub', 'positions': ['A1'] }] )

  def test_player_can_place_a_destroyer_horizontally(self):
    """
    Player can place a destroyer horizontally, and have record of its position
    """
    self.destroyer = Ship('Destroyer')
    self.player1.place_ship(self.destroyer, 'A1')
    self.assertEqual(self.player1.ships, [{'ship': 'Destroyer', 'positions': ['A1', 'A2'] }] )

  def test_player_can_place_a_cruiser_horizontally(self):
    """
    Player can place a cruiser horizontally, and have record of its position
    """
    self.destroyer = Ship('Cruiser')
    self.player1.place_ship(self.destroyer, 'A1')
    self.assertEqual(self.player1.ships, [{'ship': 'Cruiser', 'positions': ['A1', 'A2', 'A3'] }] )

  def test_player_can_place_a_destroyer_vertically(self):
    """
    Player can place a destroyer vertically, and have record of its position
    """
    self.destroyer = Ship('Destroyer')
    self.player1.place_ship(self.destroyer, 'A1', 'V')
    self.assertEqual(self.player1.ships, [{'ship': 'Destroyer', 'positions': ['A1', 'B1'] }] )

  def test_player_can_shoot_at_opponent(self):
    """
    Player can shoot at opponents board
    """
    shoot = self.player1.shoot(self.player2, 'A1')
    self.assertEqual(shoot, 'X')

  def test_player_can_hit_opponent_ship(self):
    self.ship = Ship('Destroyer')
    self.player2.place_ship(self.ship, 'A1')
    shoot = self.player1.shoot(self.player2, 'A1')
    self.assertEqual(shoot, 'HIT')

  def test_player_can_sink_ship(self):
    self.sub = Ship('Sub')
    self.player2.place_ship(self.sub, 'A1')
    shoot = self.player1.shoot(self.player2, 'A1')
    self.assertEqual(shoot, 'SUNK')

if __name__ == '__main__':
  unittest.main()