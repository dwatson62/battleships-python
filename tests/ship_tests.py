import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)
from player import *
from ship import *

class TestShip(unittest.TestCase):

  def setUp(self):
    self.sub = Ship('Sub')
    self.destroyer = Ship('Destroyer')
    self.cruiser = Ship('Cruiser')

  def test_ship_has_name_on_creation(self):
    self.assertEqual(self.sub.name, 'Sub')

  def test_throws_error_when_given_incorrect_ship(self):
    with self.assertRaises(Exception) as context:
      self.ship = Ship('Yacht')
    self.assertTrue('Ship not available' in context.exception)

  def test_sub_gets_correct_length(self):
    self.assertEqual(self.sub.length, 1)

  def test_destroyer_gets_correct_length(self):
    self.assertEqual(self.destroyer.length, 2)

  def test_destroyer_can_be_placed_vertically(self):
    self.squares = self.destroyer.get_vertical_squares('B9')
    self.assertEqual(self.squares, ['B9', 'C9'])

  def test_cruiser_can_be_placed_horizontally(self):
    self.squares = self.cruiser.get_horizontal_squares('A3')
    self.assertEqual(self.squares, ['A3', 'A4', 'A5'])

  def test_ship_cannot_be_placed_out_of_bounds(self):
    with self.assertRaises(Exception) as context:
      self.sub.check_out_of_bounds(['K10'])
    self.assertTrue('Out of bounds' in context.exception)

  def test_ship_cannot_be_placed_out_of_bounds2(self):
    with self.assertRaises(Exception) as context:
      self.cruiser.check_out_of_bounds(['A9', 'A10', 'A11'])
    self.assertTrue('Out of bounds' in context.exception)

  def test_ships_cannot_overlap(self):
    self.player = Player('Player1')
    self.player.place_ship(Ship('Destroyer'), 'A5')
    with self.assertRaises(Exception) as context:
      self.cruiser.check_overlapping(self.player, ['A6'])
    self.assertTrue('Cannot overlap ships' in context.exception)

  def test_ship_has_hit_points(self):
    self.assertEqual(self.cruiser.length, self.cruiser.hits)

if __name__ == '__main__':
  unittest.main()