import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)
from player import *
from ship import *

class TestPlayer(unittest.TestCase):

  def setUp(self):
    self.player1 = Player('Player1')
    self.player2 = Player('Player2')
    self.battleship = Ship('Battleship')

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
    self.assertEqual(self.player1.ships, [{'ship': 'Sub', 'positions': ['A1'], 'hits': 1 }] )

  def test_player_can_place_a_battleship_horizontally(self):
    """
    Player can place a Battleship horizontally, and have record of its position
    """
    self.player1.place_ship(self.battleship, 'A1')
    self.assertEqual(self.player1.ships, [{'ship': 'Battleship', 'positions': ['A1', 'A2', 'A3', 'A4'], 'hits': 4 }] )

  def test_player_can_place_a_cruiser_horizontally(self):
    """
    Player can place a cruiser horizontally, and have record of its position
    """
    self.cruiser = Ship('Cruiser')
    self.player1.place_ship(self.cruiser, 'A1')
    self.assertEqual(self.player1.ships, [{'ship': 'Cruiser', 'positions': ['A1', 'A2', 'A3'], 'hits': 3 }] )

  def test_player_can_place_a_battleship_vertically(self):
    """
    Player can place a destroyer vertically, and have record of its position
    """
    self.player1.place_ship(self.battleship, 'A1', 'V')
    self.assertEqual(self.player1.ships, [{'ship': 'Battleship', 'positions': ['A1', 'B1', 'C1', 'D1'], 'hits': 4 } ])

  def test_player_can_shoot_at_opponent(self):
    """
    Player can shoot at opponents board
    """
    shoot = self.player1.shoot(self.player2, 'A1')
    self.assertEqual(shoot, 'X')

  def test_player_can_fire_at_square_only_once(self):
    shoot = self.player1.shoot(self.player2, 'A1')
    with self.assertRaises(Exception) as context:
      self.player1.shoot(self.player2, 'A1')
    self.assertTrue('Already fired once' in context.exception)

  def test_player_cannot_shoot_outside_of_board(self):
    with self.assertRaises(Exception) as context:
      self.player1.shoot(self.player2, 'A11')
    self.assertTrue('Out of bounds' in context.exception)

  def test_player_cannot_shoot_outside_of_board2(self):
    with self.assertRaises(Exception) as context:
      self.player1.shoot(self.player2, 'A0')
    self.assertTrue('Out of bounds' in context.exception)

  def test_player_cannot_shoot_outside_of_board3(self):
    with self.assertRaises(Exception) as context:
      self.player1.shoot(self.player2, '1B')
    self.assertTrue('Out of bounds' in context.exception)

  def test_player_can_hit_opponent_ship(self):
    self.player2.place_ship(self.battleship, 'A1')
    shoot = self.player1.shoot(self.player2, 'A1')
    self.assertEqual(shoot, 'HIT')

  def test_player_can_sink_ship(self):
    self.player2.place_ship(Ship('Cruiser'), 'A1')
    self.player1.shoot(self.player2, 'A1')
    self.player1.shoot(self.player2, 'A2')
    shoot = self.player1.shoot(self.player2, 'A3')
    self.assertEqual(shoot, 'SUNK')

if __name__ == '__main__':
  unittest.main()